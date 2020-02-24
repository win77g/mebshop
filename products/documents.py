# from django_elasticsearch_dsl import Document,Index
# from django_elasticsearch_dsl.registries import registry
# from .models import Product
#
# product = Index('products')
#
# # @registry.register_document
# @product.document
# class ProductDocument(Document):
#       # class Index:
#       #   # Name of the Elasticsearch index
#       #   name = 'products'
#       #   # See Elasticsearch Indices API reference for available settings
#       #   settings = {'number_of_shards': 1,
#       #               'number_of_replicas': 0}
#
#       class Django:
#         model = Product
#         fields = [
#             'name',
#         ]
