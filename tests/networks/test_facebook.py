import uuid

from social_ids.networks import facebook


def test_get_id():
    # Using an existing page name should return the page ID
    assert facebook.get_id('getfanzone') == '1606732132871809'

    # Using an existing profile handler should return the profile ID
    assert facebook.get_id('zuck') == '4'

    # Wrong page or profile handler should return None
    assert facebook.get_id(str(uuid.uuid4())) is None
