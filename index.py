from whoosh import index, fields, qparser
import os

schema = fields.Schema(title=fields.TEXT(stored=True),description=fields.TEXT(stored=True),transcript=fields.TEXT,url=fields.STORED)

if not os.path.exists("index"):
	os.mkdir("index")
	search_index = index.create_in("index",schema)
else:
	search_index = index.open_dir("index")

queryparser = qparser.QueryParser("transcript",schema)

def search(q):
	with search_index.searcher() as s:
		results = s.search(queryparser.parse(q))
		r = list(results)
		r.sort(key=lambda x: x.rank)
		return [res.fields() for res in r]

def add_to_index(title,description,transcript,url):
	w = search_index.writer()
	w.add_document(title=title,description=description,transcript=transcript,url=url)
	w.commit()
