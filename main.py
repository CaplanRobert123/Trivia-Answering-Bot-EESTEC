import sys, requests, os, nltk
from googlesearch import search
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

query = "Who is the lead singer of band Vita de vie?"

question_text = ""
question_type = ""
question_category = ""
answer_choices = []
answer_type = ""
idx = 0

for url in search(query, num = 1, stop = 1, pause = 2):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    result = soup.find_all('p')
    
    if not os.path.exists("output"):
        os.mkdir("output")
    f = open(f"output/{idx}.txt", 'a')
    f.truncate()

    for rr in result:
        f.write(rr.get_text())

    f.close()

    idx += 1