import requests, json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}
# Force no proxy
r = requests.post(
    "https://overpass-api.de/api/interpreter",
    data='[out:json];node["place"="city"]["name"="New York"];out 1;',
    headers=headers,
    timeout=15,
    proxies={"http": None, "https": None},
)
print(f"status={r.status_code}")
if r.status_code == 200:
    d = r.json()
    for e in d.get("elements", []):
        print(f"OK: {e['tags']['name']} lat={e['lat']} lng={e['lon']}")
else:
    print(r.text[:200])
