from openpodcast.episodes import Episode
from openpodcast.podcasts import Podcast
from openpodcast.rss import RSSPodcast


def test_rss():
    """Test RSS creation """
    p = Podcast(title="Some title", description="Description")
    epi1 = Episode(podcast=p, title='Epi1 title', description='Epi1 description', published=True)
    epi2 = Episode(podcast=p, title='Epi2 title', description='Epi2 description', published=False)
    rp = RSSPodcast(podcast=p)
    epi3 = Episode(podcast=p, title='Epi3 title', description='Epi3 description', published=True)

    rss = rp.rss()

    assert f"<title>{ p.title }</title>" in rss
    assert f"<title>{ epi1.title }</title>" in rss
    assert f"<title>{ epi2.title }</title>" not in rss
    assert f"<title>{ epi3.title }</title>" in rss
    assert f"<description>{ p.description }</description>" in rss
    assert f"<description><![CDATA[{ epi1.description }]]></description>" in rss
    assert f"<description><![CDATA[{ epi2.description }]]></description>" not in rss
    assert f"<description><![CDATA[{ epi3.description }]]></description>" in rss


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
