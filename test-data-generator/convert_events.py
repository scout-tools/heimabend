import json

model = "basic.event"

result = []

with open('input/events.json') as json_file:
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
    result[i-1]['fields']['createdAt'] = event['createdAt']
    result[i-1]['fields']['createdBy'] = event['createdBy']
    result[i-1]['fields']['material'] = event['material']
    result[i-1]['fields']['costsRating'] = event['costsRating']
    result[i-1]['fields']['description'] = event['description']
    result[i-1]['fields']['executionTimeRating'] = event['executionTimeRating']
    result[i-1]['fields']['isActive'] = event['isActive']
    result[i-1]['fields']['isPrepairationNeeded'] = event['isPrepairationNeeded']
    result[i-1]['fields']['like_score'] = event['like_score']
    result[i-1]['fields']['createdByEmail'] = event['createdByEmail']

with open('output/events.json', 'w') as outfile:
    json.dump(result, outfile)
