from glob import glob
import json

def prepare_collection():
    parsed_papers = glob('../processed-papers/'+"*.json")
    all_records = [json.load(open(p,'r', encoding='utf-8')) for p in parsed_papers]
    filtered_records = []
    for rec in all_records:
        f_rec = {}
        f_rec['title'] = rec['title']
        f_rec['id'] = rec['paper_id']
        f_rec['abstract'] = rec['abstract']
        paragraphs = [r['text'] for r in rec['pdf_parse']['body_text']]
        f_rec['paragraphs'] = paragraphs
        f_rec['body'] = "\n".join(paragraphs)
        f_rec['venue'] = rec['venue']
        filtered_records.append(f_rec)
    with open("../typesense-data/tldr.jsonl",'w', encoding='utf-8') as outf:
        for rec in filtered_records:
            outf.write(json.dumps(rec))
            outf.write("\n")

if __name__ == "__main__":
    prepare_collection()