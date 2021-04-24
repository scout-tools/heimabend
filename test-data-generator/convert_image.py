import json

model = "basic.image"

result = []

with open('input/event_dump.json') as json_file:
    data = json.load(json_file)

events = data

for i, event in enumerate(events, start=1):
    result.append({
        "model": model,
        "pk": i,
        "fields": {}
    })

    result[i-1]['fields']['id'] = event['id']
    result[i-1]['fields']['image'] = event['imageLink']
    result[i-1]['fields']['uploaded_at'] = event['created_at']


with open('output/events.json', 'w') as outfile:
    json.dump(result, outfile)
