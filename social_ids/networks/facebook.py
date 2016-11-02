import re
import requests

BASE_URL = 'https://www.facebook.com/{handler}/'
PATTERN_PAGE = '\{\"pageID\"\:\"(\d+?)\"\,\"pageName\"\:\"'
PATTERN_PROFILE = '\"entity_id\"\:\"(\d+?)\"\}'

def get_id(handler):
    """Returns Facebook user/page ID for the given handler
    """
    req = requests.get(BASE_URL.format(handler=handler))

    try:
        return re.search(PATTERN_PAGE, req.text).group(1)
    except AttributeError:
        # Maybe it wasn't a Faceboog Page but a profile instead
        try:
            return re.search(PATTERN_PROFILE, req.text).group(1)
        except AttributeError:
            return None
