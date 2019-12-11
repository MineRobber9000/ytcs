import index, argparse

parser=argparse.ArgumentParser(description="Searches your index.")
parser.add_argument("query",help="Search query")
args = parser.parse_args()

results = index.search(args.query)
if len(results)==0: print("No results found.")
else:
	for i, res in enumerate(results,1):
		print("{!s}) {} ({})".format(i,res["title"],res["url"]))
