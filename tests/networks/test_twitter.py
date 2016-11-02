import uuid

from social_ids.networks import twitter


def test_get_id():
    # Using an existing twitter handler shour return the user id
    assert twitter.get_id('guillemch') == '379637011'

    # Wrong page or profile handler should return None
    assert twitter.get_id(str(uuid.uuid4())) is None
