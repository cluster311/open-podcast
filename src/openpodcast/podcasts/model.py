from openpodcast.exceptions import PodcastDescriptionTooLong
from openpodcast import settings


class Podcast:
    def __init__(self, title: str = None):
        if title is not None:
            self._title = title
        self._description = ""
        # self._published = False
        # self._ttl = 1440
        # self.language = None  # es en or es-ar en-us
        # self.country = None

        # create new objects
        self._image = None
        # self.author = None
        # self.publisher = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        if len(description) > settings.PODCAST_DESCRITION_MAX_LENGTH:
            raise PodcastDescriptionTooLong(descr_long=len(description))
        self._description = description

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
