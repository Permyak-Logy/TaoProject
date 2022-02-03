import requests
import json

response = requests.get("http://127.0.0.1/api/people/hell")
print(json.loads(response.content)[""])
