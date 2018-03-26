# Logan Czernel : Webscraping program for https://foursquare.com

from requests import get
from bs4 import BeautifulSoup

# Getting the user input 
print('Are you looking for Food, Coffee, Nightlife, Fun or Shopping?' + '\n' +
      'Type "Food" to select Food, "Coffee" to select Coffee and so on.')

def get_url():
    """
    Identifying which input they selected.
    """
    url = None
    while url == None:
        user_request = input().lower()
        if user_request == 'food':
            url = 'https://foursquare.com/explore?cat=food&mode=url&near=Dublin%2C%20Dublin%20City%2C%20Ireland&nearGeoId=72057594040892510'
        elif user_request == 'coffee':
            url = 'https://foursquare.com/explore?cat=coffee&mode=url&near=Dublin%2C%20Dublin%20City%2C%20Ireland&nearGeoId=72057594040892510'
        elif user_request == 'nightlife':    
            url = 'https://foursquare.com/explore?cat=drinks&mode=url&near=Dublin%2C%20Dublin%20City%2C%20Ireland&nearGeoId=72057594040892510'
        elif user_request == 'fun':
            url = 'https://foursquare.com/explore?cat=arts&mode=url&near=Dublin%2C%20Dublin%20City%2C%20Ireland&nearGeoId=72057594040892510'
        elif user_request == 'shopping':
            url = 'https://foursquare.com/explore?cat=shops&mode=url&near=Dublin%2C%20Dublin%20City%2C%20Ireland&nearGeoId=72057594040892510'
        else:
            print('I am sorry, but I can not identify which option you chose. Please try again: ')
    return url

# Gathering the data from of the specific url and making it useable
r = get(get_url())
soup = BeautifulSoup(r.content, 'html5lib')
g_data = soup.find_all('div', {'class': 'infoCol'} )

# Filtering through 'beautiful' data for useful information
for counter, data in enumerate(g_data):
    print('{}. '.format(counter+1) + '\n',
          'Name: ' + data.find_all('div', {'class': 'venueName'})[0].find('a').text + '\n',
          'Rating Out of 10: ' + data.find_all('div', {'class': 'venueScore positive'})[0].text + '\n',
          'Address: ' + data.find_all('div', {'class': 'venueAddress'})[0].text + '\n',
          'Category: ' + data.find_all('span', {'class': 'categoryName'})[0].text)
# Some listings, for example listings for 'fun', are free of charge.
    try:
        print(' Price Point out of €€€€: ' + data.find_all('span', {'class': 'darken'})[0].text + '\n')
    except:
        print('')


