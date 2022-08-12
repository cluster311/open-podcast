from openpodcast import Podcast, RSSPodcast


def test_rss():
    """Test RSS creation """
    p = Podcast(title="Some title", description="Description")
    rp = RSSPodcast(podcast=p)
    rss = rp.rss()

    assert f"<title>{ p.title }</title>" in rss
    assert f"<description>{ p.description }</description>" in rss
