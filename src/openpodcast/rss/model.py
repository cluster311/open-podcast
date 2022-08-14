import logging
import os
from jinja2 import Environment, FileSystemLoader
from datetime import date

from openpodcast import __VERSION__


logger = logging.getLogger(__name__)


class RSSPodcast:
    def __init__(self, podcast):
        self.podcast = podcast
        logger.info(f'Creating RSSPodcast {self.podcast.title}')
        # Use Itunes elements
        self.use_itunes = True
        # Use Googleplay elements
        self.use_google = True

    def podcast_data(self):
        """ Transform a Podcast to a dict valid to the RSS template """
        current_year = date.today().year
        data = {
            "use_itunes": self.use_itunes,
            "use_google": self.use_google,
            "podcast": self.podcast,
            "year": current_year,
            "generator": "Parlarispa",
            "generator_version": __VERSION__,
        }
        # TODO temp hacks
        data["podcast"].autor = {
            "nombre": "TODO",
            "email": "todo@todo.com"
        }
        data["podcast"].publisher = {
            "nombre": "TODO",
            "email": "todo@todo.com"
        }
        return data

    def rss(self):
        """ Get the final RSS for a given podcast """
        loader = FileSystemLoader(
            [os.path.join(os.path.dirname(__file__), "templates")]
        )
        env = Environment(loader=loader)
        template = env.get_template("rss.xml")
        data = self.podcast_data()
        return template.render(data)

    def save(self, path):
        f = open(path, "w")
        f.write(self.rss())
        f.close()
