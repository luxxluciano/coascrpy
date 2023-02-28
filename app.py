import requests
from bs4 import BeautifulSoup
import streamlit as st

# URL to scrape
url = "https://infraexam.com/ca-cyberops-associate/modules-1-2-threat-actors-and-defenders-group-exam-answers-full-100/"

# Retrieve the page content
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Find all the questions and answers
questions = soup.find_all("strong", {"style": "color: #ff0000;"})
answers = soup.find_all("div", {"style": "color: #ff0000; font-size: 18px;"})

# Create a searchable text format for questions and answers
text = ""
for i in range(len(questions)):
    text += f"{i+1}. {questions[i].text}\n"
    text += f"{answers[i].text}\n\n"

# Create Streamlit app to display the searchable text format
st.title("Exam Questions and Answers")
search_term = st.text_input("Search for a keyword:")
if search_term:
    filtered_text = [q for q in text.split("\n\n") if search_term.lower() in q.lower()]
    for q in filtered_text:
        st.write(q)
else:
    st.write(text)
