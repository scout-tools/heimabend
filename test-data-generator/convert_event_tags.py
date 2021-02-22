import json

model = "basic.event_tags"

result = []

dict_tag_ids = {
    "isPossibleInside": 46,
    "isPossibleOutside": 47,
    "isLvlOne": 50,
    "isLvlThree": 51,
    "isLvlTwo": 52,
    "isPossibleAlone": 49,
    "isPossibleDigital": 48
}

tag_keys_list = list(dict_tag_ids.keys())

with open('input/events.json') as json_file:
    events = json.load(json_file)

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

for event in events:
    for key in tag_keys_list:
        if (event[key] == 1):
            i = i + 1
            result.append({
                "model": model,
                "pk": i,
                "fields": {
                    "event_id": event['id'],
                    "tag_id": dict_tag_ids[key]
                }
            })



with open('output/event_tags.json', 'w') as outfile:
    json.dump(result, outfile)
