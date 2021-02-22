import json

model = "basic.like"

result = []


with open('input/likes.json') as json_file:
    data = json.load(json_file)

for i, event in enumerate(data, start=1):
    result.append({
        "model": model,
        "pk": i,
        "fields": {}
    })

    result[i-1]['fields']['eventId_id'] = event['eventId_id']
    result[i-1]['fields']['like_created'] = event['like_created']
    result[i-1]['fields']['opinionTypeId'] = event['opinionTypeId']

with open('output/likes.json', 'w') as outfile:
    json.dump(result, outfile)
