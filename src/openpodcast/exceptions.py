from openpodcast.settings import PODCAST_DESCRITION_MAX_LENGTH


class PodcastError(Exception):
    pass


class PodcastDescriptionTooLong(PodcastError):
    def __init__(self, descr_long, extras=""):
        msg = (
            f"Podcast description too long {descr_long}. "
            f"Max is PODCAST_DESCRITION_MAX_LENGTH={PODCAST_DESCRITION_MAX_LENGTH}."
            f"{extras}"
        )
        self.message = msg
        super().__init__(self.message)
