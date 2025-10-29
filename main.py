import requests

# Swagger
cake_id = 11
URL = f"http://127.0.0.1:8000/cakes/{cake_id}/"

response = requests.get(URL)

print(response.status_code)
print(response.json())

if response.status_code == 200:
    pass
elif response.status_code == 404:
    pass
else:
    raise RuntimeError("Some internal error occurred")