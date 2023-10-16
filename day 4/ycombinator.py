from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

headings = []
scores = []
links = []

headings = soup.find_all(class_ = 'athing')
scores = soup.find_all(class_ = 'subtext')
links = soup.find_all(class_ = 'sitestr')

for h,s,l in zip(headings, scores, links) :
    text1 = h.get_text()
    print(f"Heading : {text1}")
    text2 = s.get_text()
    print(f"Score : {text2}")
    text3 = l.get_text()
    print(f"Link : {text3}")
    print("\n\n")
    


#for s in scores :
    
    


#for l in links :