import pytest
from openpodcast import Podcast
from openpodcast.exceptions import PodcastDescriptionTooLong


def test_base_podcast_class():
    """Just some initial test"""
    p = Podcast()
    p.description = "Description"
    assert p.description == "Description"


def test_base_podcast_long_descr_errpr():
    """Test long descr"""
    p = Podcast()
    with pytest.raises(
        PodcastDescriptionTooLong, match="Podcast description too long 1000. Max is PODCAST_DESCRITION_MAX_LENGTH=512."
    ):
        p.description = "a" * 1000
    assert p.description == ""
