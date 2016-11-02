import re
import requests

BASE_URL = 'https://www.twitter.com/{}'
PATTERN = 'href\=\"\/{}" data\-user\-id\=\"(\d+?)\"\>'

def get_id(handler):
    """Returns Facebook user/page ID for the given handler
    """
    req = requests.get(BASE_URL.format(handler))

    try:
        return re.search(PATTERN.format(handler), req.text).group(1)
    except AttributeError:
        return None
