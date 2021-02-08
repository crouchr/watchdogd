import os


def get_version():
    if 'VERSION' in os.environ:
        version = os.environ['VERSION']
    else:
        version = 'IDE-1.0.0'   # i.e. running in PyCharm

    return version


def get_poll_secs():
    if 'POLL_SECS' in os.environ:
        poll_secs = int(os.environ['POLL_SECS'])
    else:
        poll_secs = 60   # i.e. running in PyCharm

    return poll_secs