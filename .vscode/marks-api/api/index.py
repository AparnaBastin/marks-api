import json
from urllib.parse import parse_qs

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    marks_map = {entry["name"]: entry["marks"] for entry in data}
    query = parse_qs(request.query_string.decode())
    names = query.get("name", [])
    marks = [marks_map.get(name, None) for name in names]

    return response.json({"marks": marks})
