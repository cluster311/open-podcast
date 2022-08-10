from schema import Schema, And, Use, Or, SchemaError


def validate_podcast(podcast):
    """ Validate all fields and settings """
    data = [podcast.as_dict]  # Schema require a list of elements to validate
    settings = podcast.settings.copy()

    schema = Schema([
        {
            'title': And(str, len),
            'description':  And(
                str,
                lambda n: len(n) < settings['description_max_length']
            ),
            'ttl':  And(
                int,
                lambda n: settings['ttl_min'] <= n <= settings['ttl_max']
            ),
            'country': Or(
                None,
                And(
                    str,
                    Use(str.lower),
                    lambda s: s in ('ar', 'us')
                )
            ),
            'language': And(
                str,
                Use(str.lower),
                lambda s: s in ('en', 'es')
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
