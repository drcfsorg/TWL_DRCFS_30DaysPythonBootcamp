# A scraper to scrape news from nepali news site


import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://www.nepalnews.com/'
page = requests.get(url)

#covid_url="https://covid19.mohp.gov.np/"
# parse the html content

soup = BeautifulSoup(page.content, 'html.parser')
articles=soup.find_all('h3')
news_articles=[]


# loop through all the articles and add them on new list 
for article in articles:
	try:
		news_articles.append(article.find_all('a')[0].text)
	except Exception:
		continue

	
print(news_articles)
sn=0
print("Top headings today")
for news in news_articles:
	print(f'''
{sn} {news}
''') 
	print("============================")
	sn+=1
