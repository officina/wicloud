# -*- coding: utf-8 -*-

# Put here your production specific settings

ADMINS = [
    ('THUX Team', 'jumbo@thux.it'),
]
EMAIL_SUBJECT_PREFIX = '[MYGENERALI_prod]'

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'https://search-wicloud-test-v4ec22jhfhzgml5llavkezercu.eu-west-1.es.amazonaws.com'
    },
}
