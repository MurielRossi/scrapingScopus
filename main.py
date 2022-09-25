import requests
import json
from pybliometrics.scopus import ScopusSearch
from datetime import datetime

start = datetime.now().replace(microsecond=0)

query = "healtcare AND artificial intelligence"

s = ScopusSearch(query, view="STANDARD", subscriber=False)
end = datetime.now().replace(microsecond=0)
risultati = s.results
print(len(s.results))

for result in risultati:
    print(result.__getattribute__("title"))





