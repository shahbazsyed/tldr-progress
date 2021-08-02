from flask import Flask, json, render_template, request, jsonify, abort, redirect, Blueprint
from api import TypeSenseSearch





TS = TypeSenseSearch()
app = Flask(__name__)
bp = Blueprint('tldr-search', __name__, template_folder='templates')

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/search", methods=["GET"])
def search():
    page_size=10
    query = request.args.get("query")
    print("Searched for {}".format(query))
    response = TS.search(query)
    print(response.keys())
    print("Found {} results".format(response['found']))
    hits = response['hits']
    print(len(hits))
    print(hits[0].keys())
    print(hits[0]['document'].keys())      
    for hit in hits:
        if query in hit['document']['title'].lower():
            print(hit['document']['title'])
            print(hit['text_match'])   
            print(hit['highlights'])
    # print(json.dumps(response, indent=4))
    return render_template('index.html', results=response['hits'])
    

if __name__ =="__main__":
    app.run(debug=True)