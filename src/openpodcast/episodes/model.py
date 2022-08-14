import logging
from uuid import uuid4

from openpodcast.exceptions import EpisodeValidationError
from openpodcast.episodes.validate import validate_episode


logger = logging.getLogger(__name__)


class Episode:
    def __init__(self, podcast, **kwargs):
        """ Creates a podcast Episode
            kwargs allow to fill any properties
        """
        self.podcast = podcast
        self.guid = uuid4().hex
        self.title = kwargs.pop("title", "")
        logger.info(f'Creating Episode {self.title}')
        self.podcast.add_episode(self)
        self.description = kwargs.pop("description", "")
        self.guid = kwargs.pop("guid", "")
        self.url = kwargs.pop("url", None)
        self.published = kwargs.pop("published", False)
        self.pub_date = kwargs.pop("pub_date", False)

        # create new objects
        self._audio = None
        self._image = None
        # self.author = None
        # self.publisher = None

        self.errors = None

    @property
    def as_dict(self):
        dct = {
            "title": self.title,
            "podcast": self.podcast.as_dict,
            "description": self.description,
            "url": self.url,
            "published": self.published,
        }
        return dct

    @property
    def is_valid(self):
        valid, errors = validate_episode(self)
        self.errors = errors if not valid else None
        return valid

    def validate(self):
        """ Validate all podcasts properties
            and raise and error if something fails
        """
        valid, errors = validate_episode(self)
        self.errors = errors if not valid else None
        if not valid:
            raise EpisodeValidationError(f"Invalid episode, check <episode>.errors")
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
