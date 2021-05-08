import requests
from bs4 import BeautifulSoup

# pages from 0 to 576060
def jobs(num):
    for i in range(0, int(num), 10):
        URL = 'https://ca.indeed.com/jobs?q=software&l='.format(i)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id='resultsCol')

        jobElems = results.find_all('div', class_='jobsearch-SerpJobCard')

        for jobElem in jobElems:
            title = jobElem.find('h2', class_='title')
            company = jobElem.find('span', class_='company')
            remote = jobElem.find('span', class_='remote')
            summary = jobElem.find('div', class_='summary')
            if None in (title, company, remote, summary):
                continue
            print(title.text.strip())
            print(company.text.strip())
            print(remote.text.strip())
            print(summary.text.strip())
            print()

