# -*- coding: utf-8 -*-

# Put here your production specific settings

ADMINS = [
    ('Wi4b Team', 'info@wi4b.it'),
]
EMAIL_SUBJECT_PREFIX = '[wicloud_prod]'

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'https://search-wicloud-test-v4ec22jhfhzgml5llavkezercu.eu-west-1.es.amazonaws.com'
    },
}
