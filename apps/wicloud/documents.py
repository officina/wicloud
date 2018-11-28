# documents.py

from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer
from .models import Installation, Gateway, Node

# Name of the Elasticsearch index
installation = Index('installations')
gateway = Index('gateways')
node = Index('nodes')
# See Elasticsearch Indices API reference for available settings
installation.settings(
    number_of_shards=1,
    number_of_replicas=0
)
gateway.settings(
    number_of_shards=1,
    number_of_replicas=0
)
node.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@installation.doc_type
class InstallationDocument(DocType):

    id = fields.IntegerField(attr='id')

    name = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    description = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    notes = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    installation_date = fields.DateField()

    class Meta:
        model = Installation
        # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000

@gateway.doc_type
class GatewayDocument(DocType):

    id = fields.IntegerField(attr='id')

    name = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    description = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    notes = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )



    class Meta:
        model = Gateway
        # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000

@node.doc_type
class NodeDocument(DocType):

    id = fields.IntegerField(attr='id')

    name = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    mac = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    log_time_ist = fields.IntegerField()
    log_time_0 = fields.IntegerField()
    log_time_1 = fields.IntegerField()
    log_time_2 = fields.IntegerField()
    log_time_3 = fields.IntegerField()
    time_zone = fields.IntegerField()
    time_zone_code = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )
    latitude = fields.FloatField()
    longitude = fields.FloatField()
    altitude = fields.FloatField()



    class Meta:
        model = Node
        # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000
