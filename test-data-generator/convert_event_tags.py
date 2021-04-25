import json

model = "basic.event_tags"

result = []

with open('input/event_tags.json') as json_file:
    event_tags = json.load(json_file)

for i, event in enumerate(event_tags, start=1):
    result.append({
        "model": model,
        "pk": i,
        "fields": {}
    })

    result[i-1]['fields']['event_id'] = event['event_id']
    result[i-1]['fields']['tag_id'] = event['tag_id']


with open('output/event_tags.json', 'w') as outfile:
    json.dump(result, outfile)
