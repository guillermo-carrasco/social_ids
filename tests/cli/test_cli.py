import uuid

from click.testing import CliRunner
from social_ids.cli import get_ids

runner = CliRunner()

def test_missing_arguments():
    result = runner.invoke(get_ids.get_id, [])
    assert result.exit_code == 2
    assert 'Missing argument' in result.output


def test_wrong_network():
    result = runner.invoke(get_ids.get_id, ['UNKNOWN_NETWORK', '123456'])
    assert result.exit_code == 2
    assert 'Invalid value' in result.output


def test_facebook():
    # Use correct id should return the ID
    result = runner.invoke(get_ids.get_id, ['facebook', 'zuck'])
    assert result.exit_code == 0
    assert '4' in result.output

    # Use incorrect id should fail
    result = runner.invoke(get_ids.get_id, ['facebook', str(uuid.uuid4())])
    assert result.exit_code == 1
    assert '¯\_(ツ)_/¯' in result.output


def test_twitter():
    # Use correct id should return the ID
    result = runner.invoke(get_ids.get_id, ['twitter', 'guillemch'])
    assert result.exit_code == 0
    assert '379637011' in result.output

    # Use incorrect id should fail
    result = runner.invoke(get_ids.get_id, ['twitter', str(uuid.uuid4())])
    assert result.exit_code == 1
    assert '¯\_(ツ)_/¯' in result.output


def test_instagram():
    # Use correct id should return the ID
    result = runner.invoke(get_ids.get_id, ['instagram', 'guillemch'])
    assert result.exit_code == 0
    assert '3408581998' in result.output

    # Use incorrect id should fail
    result = runner.invoke(get_ids.get_id, ['instagram', str(uuid.uuid4())])
    assert result.exit_code == 1
    assert '¯\_(ツ)_/¯' in result.output
