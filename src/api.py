import json
import settings
import typesense
from typesense import client


class TypeSenseSearch:
    def __init__(self):
        self.client = self.__instantiate__()

    
    def __instantiate__(self):
        client = typesense.Client({
        'nodes': [{
            'host': settings.HOST,
            'port': settings.PORT,
            'protocol': settings.PROTOCOL
            }],
        'api_key': settings.API_KEY,
        'connection_timeout_seconds': 2
        })
        return client

    def search(self, query):
        search_parameters = {
        'q'         : query,
        'query_by'  : 'title, abstract'
        }
        response = self.client.collections['tldr-papers'].documents.search(search_parameters)
        return response
    
