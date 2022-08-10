from openpodcast.exceptions import PodcastValidationError
from openpodcast.podcasts.validate import validate_podcast


class Podcast:
    def __init__(self, **kwargs):
        """ Starts a podcasts
            kwargs allow to fill any properties and settings
        """

        self.title = kwargs.pop("title", "")
        self.description = kwargs.pop("description", "")
        self.url = kwargs.pop("url", None)
        self.published = kwargs.pop("published", False)
        # The <ttl> (ttl=time to live) element specifies the number of minutes the
        # feed can stay cached before refreshing it from the source.
        self.ttl = kwargs.pop("ttl", 1440)
        self.language = kwargs.pop("language", "en")
        self.country = kwargs.pop("country", None)

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
        dct = {
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "published": self.published,
            "ttl": self.ttl,
            "language": self.language,
            "country": self.country,
        }
        return dct

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
