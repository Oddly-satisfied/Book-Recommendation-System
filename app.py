import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity
import re
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
df = pd.read_csv("books.csv")

# Combine relevant columns for recommendations
df['details'] = df['Title'] + ' ' + df['genres'] + ' ' + df['Author'] + ' ' + df['publisher']
df['details'] = df['details'].fillna('')

# Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['details'])

# Calculate cosine similarity
cosineSimilarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommendations(title, cosineSimilarity=cosineSimilarity):
    keywords = re.findall(r'\w+', title.lower())
    pattern = '|'.join(keywords)
    # Broaden the search to include related genres and authors as well
    matching_titles = df[df['Title'].str.contains(pattern, case=False, na=False) |
                         df['genres'].str.contains(pattern, case=False, na=False) |
                         df['Author'].str.contains(pattern, case=False, na=False)]
    
    if matching_titles.empty:
        return "No books found matching that title."
    
    id = matching_titles.index[0]
    similarityScores = sorted(list(enumerate(cosineSimilarity[id])), key=lambda x: x[1], reverse=True)
    
    # Get the top N recommendations
    top_n_indices = [score[0] for score in similarityScores[1:100]]
    random_recommendations = random.sample(top_n_indices, min(10, len(top_n_indices)))

    return df['Title'].iloc[random_recommendations], df['isbn13'].iloc[random_recommendations]

# Function to get cover URL
def get_cover_url(isbn13):
    return f"https://covers.openlibrary.org/b/isbn/{isbn13}-L.jpg"

# Streamlit app setup
st.title("Book Recommendation System")
title = st.text_input("Enter a book title:")

if st.button("Search"):
    recommended_books, recommended_isbns = recommendations(title)
    
    if isinstance(recommended_books, str):
        st.write(recommended_books)  # Display the message if no books are found
    else:
        for book, isbn in zip(recommended_books, recommended_isbns):  # Use zip to iterate together
            st.write(book)  # Display book title
            st.image(get_cover_url(isbn), width=100)  # Display book cover