import os
import logging

from django.core.files.storage import get_storage_class
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PIL import Image


logger = logging.getLogger('file')
default_storage = get_storage_class()


class ThumbnailStorage(default_storage):

    def _save(self, name, content):

        logger.info("_save: %s %s", name, content)
        if hasattr(content, 'content_type'):
            if content.content_type.startswith('image/'):
                self.generate_thumbnails(name, content)
        return super()._save(name, content)

    def generate_thumbnails(self, name, content):

        name1, ext1 = os.path.splitext(name)
        fname, ext = os.path.splitext(content.name)

        im = Image.open(content)
        w, h = im.size
        im.thumbnail((w/3, h/3))
        dest_filename = f'{name1}_1x{ext}'
        fh = default_storage().open(dest_filename, 'wb')
        im.save(fh)
        fh.close()
        logger.info("Generato file %s", dest_filename)

        im2 = Image.open(content)
        im2.thumbnail((w*2/3, h*2/3))
        dest_filename = f'{name1}_2x{ext}'
        fh = default_storage().open(dest_filename, 'wb')
        im2.save(fh)
        fh.close()
        logger.info("Generato file %s", dest_filename)

    def get_available_name(self, name, max_length=1000):
        filename = os.path.join(settings.MEDIA_ROOT, name)
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        return name


class TestStorage(FileSystemStorage):
    """A storage that doesn't create a new file name
    """

    def get_available_name(self, name, max_length=1000):
        filename = os.path.join(settings.MEDIA_ROOT, name)
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        return name
