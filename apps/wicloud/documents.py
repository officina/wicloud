# documents.py

from django_elasticsearch_dsl import DocType, Index
from .models import Installation

# Name of the Elasticsearch index
installation = Index('installations')
# See Elasticsearch Indices API reference for available settings
installation.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@installation.doc_type
class InstallationDocument(DocType):
    class Meta:
        model = Installation
        # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',

            'description',
            'notes',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000
