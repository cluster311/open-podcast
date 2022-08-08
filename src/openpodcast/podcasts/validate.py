from openpodcast.validators import validate_int, validate_string


def validate_description(description, settings):
    errors = []
    valid, error = validate_string(description, max_length=settings["description_max_length"])
    if not valid:
        errors.append(error)
    return len(errors) == 0, errors


def validate_ttl(ttl, settings):
    errors = []
    valid, error = validate_int(ttl, max_value=settings["ttl_max"])
    if not valid:
        errors.append(error)

    return len(errors) == 0, errors


def validate_podcast(podcast):
    """ Validate all fields and settings """
    final_errors = {}
    valid, errors = validate_description(podcast.description, podcast.settings.copy())
    if not valid:
        final_errors["description"] = errors
    valid, errors = validate_ttl(podcast.ttl, podcast.settings.copy())
    if not valid:
        final_errors["ttl"] = errors

    return len(final_errors) == 0, final_errors
