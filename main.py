from datetime import datetime

from pybliometrics.scopus import ScopusSearch
import pandas as pd

import downloader as autdown


start = datetime.now().replace(microsecond=0)

query = "healthcare AND artificial intelligence AND machine learning"

# s = ScopusSearch(query, view="STANDARD", subscriber=True, kwsd="count=50")
# s = Search(query, "ScopusSearch", subscriber=True, refresh = False, max_entries= 5000, count=90, start = 0,view = "STANDARD")

s = ScopusSearch(query, refresh=False, view="STANDARD", verbose=False, download=False, integrity_fields=None, integrity_action="raise", subscriber=False, kwds="count=50")
end = datetime.now().replace(microsecond=0)
print(s.get_results_size())
risultati= [[]]
print(s.__getattribute__('title'))
print(((s.results)[0]).__getattribute__('title'))

for risultato in risultati:
    print(risultato)

row = []


autdown.execute("./acceptedInstance.csv")
autdown.execute("./acceptedInstance1.csv")
autdown.execute("./acceptedInstance2.csv")
autdown.execute("./acceptedInstance3.csv")
