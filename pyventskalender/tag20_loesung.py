# %%
import requests
from cat_fact.client import CatClient

cat_client = CatClient(requests.Session(), "http://cat-fact.herokuapp.com")
fakt = cat_client.get_random_fact("cat")

fakt["text"]