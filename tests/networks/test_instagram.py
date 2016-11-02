import uuid

from social_ids.networks import instagram


def test_get_id():
    # Using an existing profile name should return the profile ID
    assert instagram.get_id('guillemch') == '3408581998'

    # Using an existing private account handler should return the profile ID
    assert instagram.get_id('fanztest1') == '3062915768'

    # Wrong page or profile handler should return None
    assert instagram.get_id(str(uuid.uuid4())) is None
