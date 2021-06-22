import json

model = "basic.event_tags"

result = []

with open('input/event_dump.json') as json_file:
    events = json.load(json_file)

for i, event in enumerate(events, start=2212):
    result.append({
        "model": model,
        "pk": i,
        "fields": {
            "event_id": event['id'],
            "tag_id": 74

        }
    })

with open('output/new_tags.json', 'w') as outfile:
    json.dump(result, outfile)
