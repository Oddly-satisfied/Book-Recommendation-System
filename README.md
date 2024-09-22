# Book Recommendation System

## Overview

The Book Recommendation System is a web application designed to help users discover new books based on their interests. Utilizing a combination of Natural Language Processing (NLP) and cosine similarity, this system provides personalized book recommendations based on user input.

## Goals

The primary goals of the Book Recommendation System are:

- **Personalized Recommendations**: To provide users with tailored book suggestions based on their input titles, improving their reading experience.
- **Diverse Book Selection**: To include a wide range of books from various genres and authors, ensuring that users discover new and diverse reading materials.
- **User-Friendly Interface**: To create an intuitive and engaging interface using Streamlit, making it easy for users to search for books and view recommendations.
- **Randomized Recommendations**: To offer a randomized selection of recommendations from the top suggestions, encouraging users to explore different books they might not have considered.
- **Visual Appeal**: To enhance the user experience by displaying book covers, providing a more visual and attractive way to browse recommendations.
- **Continuous Improvement**: To gather user feedback for future enhancements, ensuring the system evolves and meets user needs over time.

## Features

- **Search Functionality**: Users can input the title of a book, and the system will return similar titles.
- **Random Recommendations**: Recommendations are provided randomly from the top matches to enhance user experience and discovery.
- **Book Cover Display**: Each recommendation is accompanied by the book cover image for better visual identification.

## Technologies Used

- **Python**: The core programming language for backend development.
- **Pandas**: Used for data manipulation and analysis.
- **Scikit-learn**: For implementing the TF-IDF vectorization and cosine similarity calculations.
- **Streamlit**: Framework used to create the interactive web application.
- **Regular Expressions**: For processing and matching book titles.

## Dataset Used

The Book Recommendation System utilizes the **Goodreads-books-with-genres Dataset**, which includes the following key columns:

- **Book Id**: The book identification.
- **Title**: The title of the book.
- **Author**: The author(s) of the book.
- **Genres**: The genres associated with the book.
- **Publisher**: The publisher of the book.
- **ISBN**: The International Standard Book Number (ISBN) for the book.
- **ISBN-13**: The 13 digit ISBN derived from the original ISBN-10 number.
- **Average Rating**: The average rating of the book.
- **Number of Pages**: The total number of pages in the book.
- **Ratings Count**: The total number of ratings the book has received.
- **Text Reviews Count**: The total number of reviews written about the book.
- **Publication Date**: The date the book was published.
- **Language Code**: The language the book is written in.

### Dataset Source

[Kaggle](https://www.kaggle.com/datasets/middlelight/goodreadsbookswithgenres)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Oddly-satisfied/Book-Recommendation-System.git
   cd Book-Recommendation-System

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.
