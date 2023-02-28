import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape(url):
    """
    Scrape the given URL and extract questions and answers from the unordered list with bullets.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ul = soup.find('ul')
    questions = []
    answers = []
    for li in ul.find_all('li'):
        # Extract question from the bullet point
        question = li.contents[0].strip()
        # Extract answer from the red-colored text
        answer = li.find('font', {'color': 'red'}).text.strip()
        questions.append(question)
        answers.append(answer)
    return questions, answers

# Set up the Streamlit app
st.title("Scraped Questions and Answers")
url = st.text_input("Enter URL:")
if url:
    # Scrape the URL and display the results in a searchable text format
    questions, answers = scrape(url)
    search_text = st.text_input("Search for questions or answers:")
    for i in range(len(questions)):
        if search_text.lower() in questions[i].lower() or search_text.lower() in answers[i].lower():
            st.write(f"Question {i+1}: {questions[i]}")
            st.write(f"Answer {i+1}: {answers[i]}")
