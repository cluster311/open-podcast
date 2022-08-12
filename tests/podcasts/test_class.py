import pytest
from openpodcast.podcasts import Podcast
from openpodcast.exceptions import PodcastValidationError


def test_base_podcast_class():
    """Just some initial test"""
    p = Podcast(title="Some title")
    p.description = "Description"
    assert p.description == "Description"
    assert p.is_valid
    assert p.errors is None


def test_missing_title():
    """Just some initial test"""
    p = Podcast()
    assert not p.is_valid
    assert "Key 'title' error:" in p.errors
    assert "len('') should evaluate to True" in p.errors


def test_long_descr_errpr():
    """ Test long descr raises PodcastValidationError
        while "validate()"
    """

    bad_description = "a" * 1000
    p = Podcast(title="Some title", description=bad_description)
    with pytest.raises(PodcastValidationError):
        p.validate()
    assert "Key 'description' error:" in p.errors


def test_custom_long_descr_errpr():
    """ Test(custom) long descr raises PodcastValidationError
        while "validate()"
    """

    bad_description = "a" * 11
    p = Podcast(
        title="Some title",
        description_max_length=10,
        description=bad_description
    )
    with pytest.raises(PodcastValidationError):
        p.validate()
    assert "Key 'description' error:" in p.errors


def test_bad_type_ttl():
    """ Test bad type ttl raises PodcastValidationError
        while "validate()"
    """

    p = Podcast(title="Some title", ttl="1440")
    with pytest.raises(PodcastValidationError):
        p.validate()
    assert "Key 'ttl' error:" in p.errors
    assert "'1440' should be instance of 'int'" in p.errors


def test_big_ttl():
    """ Test big ttl raises PodcastValidationError
        while "validate()"
    """

    p = Podcast(title="Some title", ttl=1440 * 8)
    with pytest.raises(PodcastValidationError):
        p.validate()
    assert "Key 'ttl' error:" in p.errors
