from schema import Schema, And, Use, Or, SchemaError


def validate_episode(episode):
    """ Validate all fields """
    podcast = episode.podcast
    data = [episode.as_dict]  # Schema require a list of elements to validate
    settings = podcast.settings.copy()

    schema = Schema([
        {
            'podcast': dict,
            'title': And(str, len),
            'description':  And(
                str,
                lambda n: len(n) < settings['description_max_length']
            ),
            'published': bool,
            'url': Or(
                None,
                And(
                    str,
                    Use(str.lower),
                    lambda s: s.startswith('http')
                )
            ),
        }
    ])
    errors = None
    valid = True
    try:
        schema.validate(data)
    except SchemaError as e:
        valid = False
        errors = e.autos
        print(f'{type(errors)} :: {errors}')
    return valid, errors
