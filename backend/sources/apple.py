
from pprint import pprint
import requests
import simplejson as json
from urllib import urlencode

MEDIA_TYPES = ['movie', 'podcast', 'musicVideo', 'audiobook', 'shortFilm', 'tvShow', 'software', 'ebook', 'all']

def request(keywords, media_type='all'):
    """
    Makes a request to the apple search api. 
    see http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html
    """
    paramaters = {
        'term': keywords,
        'media': media_type,
        'limit': 200,
    }
    paramaters = urlencode(paramaters)
    url = "http://itunes.apple.com/search?%s" % paramaters
    r = requests.get(url)

    response = json.loads(r.text)
    return response
