import json

model = "basic.event"

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
    result[i-1]['fields']['title'] = event['title']
    result[i-1]['fields']['description'] = event['description']
    result[i-1]['fields']['costs_rating'] = event['costsRating']
    result[i-1]['fields']['execution_time'] = event['executionTimeRating']
    result[i-1]['fields']['difficulty'] = 1

    result[i-1]['fields']['created_by_email'] = event['createdByEmail']
    result[i-1]['fields']['created_at'] = event['createdAt']
    result[i-1]['fields']['updated_at'] = event['updatedAt']
    result[i-1]['fields']['created_by'] = event['createdBy']
    result[i-1]['fields']['header_image_id'] = event['id']
    result[i-1]['fields']['is_active'] = event['isActive']


with open('output/events.json', 'w') as outfile:
    json.dump(result, outfile)
