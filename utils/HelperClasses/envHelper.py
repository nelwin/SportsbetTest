def get(env, *keys):
    """
    Get value of *keys (nested) in 'env' (dict)
    Return "" if not found
    :param env:
    :param keys:
    :return:
    """

    if not isinstance(env, dict):
        raise AttributeError('env.get() expects dict as first arguement')
    if len(keys) == 0:
        raise AttributeError('env.get() expects at least two arguements, one given')

    _element = env
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return ""
    return _element


def exists(env, *keys):
    '''
    Check if *keys (nested) exists in env (dict)
    :param env:
    :param keys:
    :return:
    '''
    if not isinstance(env, dict):
        raise AttributeError(f'env.exists() expects dict as first arguement: {keys}')
    if len(keys) == 0:
        raise AttributeError('env.exists() expects at least two arguements, one given')

    _element = env
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True


def getPath(env, path: str, default: str = None):
    '''
    Get value based on '.' separated path
    For example: path = common.data.msid.exp_response_get_fields
    :param env:
    :param path:
    :param default:
    :return:
    '''
    if not isinstance(env, dict):
        raise AttributeError(f'env.getPath() expects dict as first arguement: {path}')
    keys = path.split('.')
    if len(keys) == 0:
        raise AttributeError('env.getPath() expects a path, None provided')

    _element = env
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return default
    return _element
