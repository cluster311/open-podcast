from openpodcast.podcasts import Podcast
from openpodcast.rss import RSSPodcast


def test_rss():
    """Test RSS creation """
    p = Podcast(title="Some title", description="Description")
    rp = RSSPodcast(podcast=p)
    rss = rp.rss()

    assert f"<title>{ p.title }</title>" in rss
    assert f"<description>{ p.description }</description>" in rss


def test_save_rss():
    """Test RSS creation """
    p = Podcast(title="Some title", description="Description")
    rp = RSSPodcast(podcast=p)
    rp.save("tests/rss.xml")

    f = open("tests/rss.xml")
    text = f.read()
    f.close()

    assert f"<title>{ p.title }</title>" in text
    assert f"<description>{ p.description }</description>" in text
