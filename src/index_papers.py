import typesense
import json

from typesense import client


# define paper schema
papers_schema = {
  'name':'tldr-papers',
  'fields': [
    {'name':'title', 'type':'string'},
    {'name':'id', 'type':'string'},
    {'name':'abstract', 'type':'string'},
    {'name':'body', 'type':'string'},
    {'name':'venue', 'type':'string', 'facet':True}
  ]
}

# create client
def create_client():
  client = typesense.Client({
    'nodes':[{
        'host':'localhost',
        'port':'8108',
        'protocol':'http'
    }],
    'api_key': 'e5570aa0-5d05-4246-bdef-a74705a44d0a',
    'connection_timeout_seconds':2
    })
  return client

# index collections
def index_papers():
  records = [json.loads(a) for a in open('../typesense-data/tldr.jsonl','r', encoding='utf-8').readlines()]
  print("Found {} papers to index".format(len(records)))
  client = create_client()
  client.collections.create(papers_schema)
  for rec in records:
    client.collections['tldr-papers'].documents.create(rec)

# search
def search(query, query_by, from_page):
  search_parameters = {
    'q'         : query,
    'query_by'  : query_by,
    'page': from_page
    }
  client = create_client()
  response = client.collections['tldr-papers'].documents.search(search_parameters)
  return response

def get_collections():
  client = create_client()
  return client.collections.retrieve()


if __name__ == "__main__":
  query = "cloze reward"
  query_by = "title, abstract"
  from_page = 1
  result = search(query, query_by, from_page)
  print("Found {} papers out of {} in total".format(result['found'], result['out_of']))
  hits = result['hits']
  for hit in hits:
    print(hit['document']['title'])
    print("----------------")

