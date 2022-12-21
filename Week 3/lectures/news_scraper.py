'''
NOTE 

It is not allowed to scrape any website without permission. Before attempting to scrape any website,
you must check the website's robots.txt file to see what parts of the website are permitted to be scraped. 
Scraping a website without permission is a violation of the website's terms of service and can result in legal consequences.

Please make sure to respect the website's rules and only scrape the portions of the website that are allowed. 
If you have any questions about what is and is not allowed, please reach out to the website's administrator for clarification.

'''

# A scraper to scrape news from nepali news site



import requests
from bs4 import BeautifulSoup

url = 'https://www.nepalnews.com/'


def news_scraper(url:str) -> list:
    page = requests.get(url)
    news=[]
    # parse the html content
    soup = BeautifulSoup(page.content, 'html.parser')
    articles=soup.find_all('h3')

    # you can see the nested try exeption form below
    for article_title in articles:
        try:
            news.append(article_title.find_all('a')[0].text)
        except Exception:   
            try:
                news.append(article_title.find_all('span')[0].text)
            except Exception:
                continue
    return news

# First lets make a new file for storing our news articles title
def file_creator(name:str) -> None:
    with open(name,'w') as file:
        file.write("============= Today's Top Headings ===============")
        file.write('\n')
        file.write('\n')


# loop through all the articles and add them on new list
def news_artilces_saver(filename:str):
    sn=0
    articles=news_scraper(url)
    file_creator(filename)
    for title in articles:
        print(title)
        file=open(filename,'a')
        file.write(f"{sn}  {title}")
        file.write("\n")
        file.close()
        sn+=1

    
    # append the value of sn for indexing
    
# give your filename


if __name__=="__main__":
    news_artilces_saver("mero_news.txt")
