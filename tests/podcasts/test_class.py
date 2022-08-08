import pytest
from openpodcast import Podcast
from openpodcast.exceptions import PodcastValidationError


def test_base_podcast_class():
    """Just some initial test"""
    p = Podcast()
    p.description = "Description"
    assert p.description == "Description"


def test_base_podcast_long_descr_errpr():
    """ Test long descr raises PodcastValidationError
        while "validate()"
    """

    bad_description = "a" * 1000
    p = Podcast(description=bad_description)
    with pytest.raises(PodcastValidationError):
        p.validate()
    assert "description" in p.errors


def test_base_podcast_custom_long_descr_errpr():
    """ Test(custom) long descr raises PodcastValidationError
        while "validate()"
    """

    bad_description = "a" * 11
    p = Podcast(description_max_length=10, description=bad_description)
    with pytest.raises(PodcastValidationError):
        p.validate()
    assert "description" in p.errors
