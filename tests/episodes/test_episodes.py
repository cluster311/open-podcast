from openpodcast.episodes import Episode
from openpodcast.podcasts import Podcast
# from openpodcast.exceptions import EpisodeValidationError


def test_base_episode_class():
    """Just some initial test"""
    p = Podcast(title="Some title", description="Description")
    epi = Episode(podcast=p, title='Epi title', description='Epi description')
    assert epi.is_valid


def test_missing_title():
    p = Podcast(title="Some title", description="Description")
    epi = Episode(podcast=p)
    assert not epi.is_valid
    assert "Key 'title' error:" in epi.errors
    assert "len('') should evaluate to True" in epi.errors
