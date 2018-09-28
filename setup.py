# http://www.28lines.com/?p=8

import os
import re
from setuptools import setup, find_packages
from setuptools.command.test import test


class TestRunner(test):

    def run(self, *args, **kwargs):
        if self.distribution.install_requires:
            self.distribution.fetch_build_eggs(
                self.distribution.install_requires)
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(
                self.distribution.tests_require)
        from web.tests.runtests import runtests

        runtests()


def get_data_files(*args, **kwargs):
    EXT_PATTERN = kwargs.get('ext') or '\.(html|js|txt|css|po|mo)'

    data_dict = {}
    for pkg_name in args:
        data_files = []
        for dirpath, dirnames, filenames in os.walk(pkg_name):
            rel_dirpath = re.sub("^" + pkg_name + '/', '', dirpath)
            # Ignore dirnames that start with '.'
            for i, dirname in enumerate(dirnames):
                if dirname.startswith('.'):
                    del dirnames[i]
            if filenames:
                data_files += [os.path.join(rel_dirpath, f) for f in filenames
                               if re.search(EXT_PATTERN, f)]
        data_dict[pkg_name] = data_files
    return data_dict


setup(
    name='setupTest',
    version="1.0",
    description='Project Description',
    author='THUX Team',
    url='http://hg.thundersystems.it/jmb/setupTest',
    author_email='jumbo@thux.it',
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
    test_suite="web.tests",
    cmdclass={"test": TestRunner},
    install_requires=[
        'setuptools',
        'django==1.11.13',
        'django-application-settings',
        'django-extensions',
        'django-debug-toolbar',
        'django-flat-responsive',
        'djangorestframework',
        'django-cors-headers',
        'djangorestframework-jwt',
        'django-rest-auth',
        'docutils',
        'dj-cmd',
        'psycopg2-binary',
        'Pillow',
        'requests',
        'pathlib',
        'boto3',
        'django-storages',  # to upload file on S3
        'Playoff',
    ],
    package_data=get_data_files('web')
)
