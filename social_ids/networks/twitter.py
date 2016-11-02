import re
import requests

BASE_URL = 'https://www.twitter.com/{handler}'
PATTERN = 'href\=\"\/{handler}" data\-user\-id\=\"(\d+?)\"\>'

def get_id(handler):
    """Returns Twitter user ID for the given handler
    """
    req = requests.get(BASE_URL.format(handler=handler))

    try:
        return re.search(PATTERN.format(handler=handler), req.text, re.IGNORECASE).group(1)
    except AttributeError:
        return None
