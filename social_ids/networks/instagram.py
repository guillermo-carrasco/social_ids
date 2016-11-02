import re
import requests

BASE_URL = 'https://www.instagram.com/{}'
PATTERN_PUBLIC = '\"owner\"\: \{\"id\"\: \"(\d+?)\"\}'
# Instagram private pages are not gonna show any post, so you can just search for "id": "
PATTERN_PRIVATE = '\"id\": \"(\d+?)\"'

def get_id(handler):
    """Returns Instagram user ID for the given handler
    """
    req = requests.get(BASE_URL.format(handler))

    try:
        return re.search(PATTERN_PUBLIC, req.text).group(1)
    except AttributeError:
        # Try private account pattern
        try:
            return re.search(PATTERN_PRIVATE, req.text).group(1)
        except AttributeError:
            return None
