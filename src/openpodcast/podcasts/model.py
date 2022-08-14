import logging
from uuid import uuid4

from openpodcast.exceptions import PodcastValidationError
from openpodcast.podcasts.validate import validate_podcast


logger = logging.getLogger(__name__)


class Podcast:
    def __init__(self, **kwargs):
        """ Starts a podcasts
            kwargs allow to fill any properties and settings
        """
        self.title = kwargs.pop("title", "")
        logger.info(f'Creating Podcast {self.title}')
        self.guid = uuid4().hex
        self.description = kwargs.pop("description", "")
        self.url = kwargs.pop("url", None)
        self.published = kwargs.pop("published", False)
        # The <ttl> (ttl=time to live) element specifies the number of minutes the
        # feed can stay cached before refreshing it from the source.
        self.ttl = kwargs.pop("ttl", 1440)
        self.language = kwargs.pop("language", "en")
        self.country = kwargs.pop("country", None)

        self._episodes = []
        # create new objects
        self._image = None
        # self.author = None
        # self.publisher = None

        self.settings = {
            "description_max_length": 512,
            "ttl_min": 1440,  # one day default min
            "ttl_max": 1440 * 7,  # one week default max
        }

        self.settings.update(**kwargs)
        self.errors = None

    @property
    def as_dict(self):
        episodes = [episode.as_dict for episode in self.get_episodes()]
        dct = {
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "published": self.published,
            "ttl": self.ttl,
            "language": self.language,
            "country": self.country,
            "episodes": episodes,
        }
        return dct

    def add_episode(self, episode):
        logger.info(f'Adding episode {episode.title}')
        self._episodes.append(episode)

    def get_episodes(self, only_published=True):
        logger.info(f'Getting episodes {self.title}')
        if only_published:
            episodes = [episode for episode in self._episodes if episode.published]
        else:
            episodes = self._episodes
        logger.info(f'{len(episodes)} episodes returned')
        return episodes

    @property
    def is_valid(self):
        valid, errors = validate_podcast(self)
        self.errors = errors if not valid else None
        return valid

    def validate(self):
        """ Validate all podcasts properties
            and raise and error if something fails
        """
        valid, errors = validate_podcast(self)
        self.errors = errors if not valid else None
        if not valid:
            raise PodcastValidationError(f"Invalid podcast, check <podcast>.errors")
        self.errors = None
        return True

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        """Image setter
        TODO validate, save locally, set up real path
        TODO allow plugins to publish this to S3, GCD, etc
        """
        self._image = image
