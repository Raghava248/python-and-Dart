#web Scraping
from bs4 import *
with open('C:\\Users\\SAI RAGHAVENDRA\\Desktop\\page.html','r') as html_file:
    #read the html file
    page = html_file.read()
    #create instance for BeautifulSoup to parse document
    soup = BeautifulSoup(page,'html.parser')
    #look for tag p and print each review
    for p in soup.find_all('p'):
        print(p.get_text())
        
#Sentiment Analysis
from textblob import *
positive,negative = 0,0
for p in soup.find_all('p'):
    text = p.get_text()
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment >= 0:
        positive+=1
    else:
        negative+=1
print("Positive review: %d" %(positive))
print("Negative review: %d" %(negative))
