import json

def as_json(obj, **fields):
    data = {getattr(obj, key, default) for key, default in fields.items()}
    return json.dumps(data)

