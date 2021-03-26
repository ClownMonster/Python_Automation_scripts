'''
 Scraps the subscriber count of any youtube channel

'''


from bs4 import BeautifulSoup as bs 
import requests

try:
    option = int(input('Press 1 to Enter Channel Name or Press 2 to paste the url of the channel: '))
    if option == 1:
        name = input('Enter the Name of the channel: ')
        url = f'https://www.youtube.com/user/{name}'
    elif option == 2:
        url = input('Paste the url of the channel home page : ')
    else:
        raise Exception('Invalid Option')

    r = requests.get(url)
    if r.status_code == 200:
        soup = bs(r.text, 'html.parser')
        subscribers_count = soup.findAll('span', {'class': 'yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip'})
        for sub in subscribers_count:
            print('Total Subscribers in the channel : ',sub.get_text())
    else:
        if option == 1:
            raise Exception('Invalid Username Of the Channel ')
        else:
            raise Exception('Invalid Url of the Channel')


except Exception as e:
    print(e)