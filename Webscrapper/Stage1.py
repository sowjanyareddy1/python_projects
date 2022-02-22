# load the necessary libraries
import requests, json
url = input()
r = requests.get(url)
# check if the page is loading 
if r.status_code == 200:
    try:
      # use json to get the data of the page
        r.json()
        print(r.json()['content'])
    except (KeyError, json.decoder.JSONDecodeError):
        print('\nInvalid quote resource!')
else:
    print('\nInvalid quote resource!')
