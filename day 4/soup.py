from bs4 import BeautifulSoup
file=open("index.html")
contents=file.read()
file.close()
soup=BeautifulSoup(contents,"html.parser")
#print(soup.prettify())
#print(soup.title)
#print(soup.a)
#print(soup.find_all(name="a"))

#p=soup.find_all(name="p")
#print(soup.p.text)

#getting all links and extracting text from these links
#all_links=soup.find_all(name="a")
#for link in all_links:
    #print(link.getText())

#first_heading=soup.find(name="h1")
#print(first_heading.getText())

heading=soup.find(name="color")
print(heading.getText())

file.read()

