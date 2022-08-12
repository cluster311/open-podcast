import os
from jinja2 import Environment, FileSystemLoader


class RSSPodcast:
    def __init__(self, podcast):
        self.podcast = podcast

    def podcast_data(self):
        """ Transform a Podcast to a dict valid to the RSS template """
        data = {
            "podcast": self.podcast.as_dict,
            "year": 1988  # TODO current year
        }
        # TODO temp hacks
        data["podcast"]["autor"] = {
            "nombre": "TODO",
            "email": "todo@todo.com"
        }
        data["podcast"]["publisher"] = {
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
