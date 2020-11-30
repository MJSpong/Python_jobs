import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

#print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    python = job_elem.find('h2', string=lambda text: 'python' in text.lower())
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    if job_elem.find('a'):
    	link = job_elem.find('a')['href']
    	print(f"Apply here: {link}\n")
    if python:
    	print("Contains a reference to python")
    print()
    
#Note that we can pass an anonymous function to the string= argument. The 
#lambda function looks at the text of each <h2> element, converts it to 
#lowercase, and checks whether the substring 'python' is found anywhere.

#Also note that we can treat a tag (which is the object output by the find
#method) like a dictionary, in order to extract its attributes.
#Python Webscrapers
