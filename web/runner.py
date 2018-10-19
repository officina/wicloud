# a runner

from django.conf import settings
from django.test.runner import DiscoverRunner


class GeneraliDiscoverRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        settings.DEFAULT_FILE_STORAGE = 'web.storage.TestStorage'
        super().__init__(*args, **kwargs)