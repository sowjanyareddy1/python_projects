import requests, json
from bs4 import BeautifulSoup

url = input('Input the URL:\n')
response = requests.get(url,  headers={'Accept-Language': 'en-US,en;q=0.5'})
if response.status_code == 200:
    try:
        # use beautifulsoup to get the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # get the title using soup
        title = soup.h1.text
        # for getting the description get testid of span in htm by inspecting the page
        description = soup.find('span', {'data-testid':'plot-l'}).text
        date1 = soup.find('span', class_='TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex').text
        # storing those results in dictionary
        result  = {"title": title, "description": description, "date": date1}
        print(result)
    except:
        print('\nInvalid movie page!')
else:
    print('\nInvalid resource!')
