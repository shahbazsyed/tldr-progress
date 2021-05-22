import typesense
import json

# open connection
client = typesense.Client({
    'nodes':[{
        'host':'localhost',
        'port':'8108',
        'protocol':'http'
    }],
    'api_key': 'e5570aa0-5d05-4246-bdef-a74705a44d0a',
    'connection_timeout_seconds':2
})

# define schema
books_schema = {
  'name': 'books',
  'fields': [
    {'name': 'title', 'type': 'string' },
    {'name': 'authors', 'type': 'string[]' },
    {'name': 'image_url', 'type': 'string' },

    {'name': 'publication_year', 'type': 'int32' },
    {'name': 'ratings_count', 'type': 'int32' },
    {'name': 'average_rating', 'type': 'float' },

    {'name': 'authors_facet', 'type': 'string[]', 'facet': True },
    {'name': 'publication_year_facet', 'type': 'string', 'facet': True },
  ],
  'default_sorting_field': 'ratings_count'
}

# create collection
#client.collections.create(books_schema)

# # add documents to collection
# with open('../typesense-data/books.jsonl') as infile:
#   for json_line in infile:
#     book_document = json.loads(json_line)
#     client.collections['books'].documents.create(book_document)


# search collection
search_parameters = {
  'q'         : 'harry',
  'query_by'  : 'title',
  'filter_by' : 'publication_year:<1998',
  'sort_by'   : 'publication_year:desc'
}

response = client.collections['books'].documents.search(search_parameters)
print(response['found'])

