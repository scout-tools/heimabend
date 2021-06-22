import json


result_image = []
result_image_meta = []

with open('input/event_dump.json') as json_file:
    events = json.load(json_file)

for i, event in enumerate(events, start=0):

    if (event['imageLink'] is not None):
        result_image.append({
            "model": "basic.image",
            "pk": i + 1,
            "fields": {}
        })
        j = len(result_image) - 1
        result_image[j]['fields']['id'] = event['id']
        result_image[j]['fields']['image'] = 'image/{}.jpeg'.format(event['imageLink'])
        result_image[j]['fields']['created_at'] = event['created_at']

        result_image_meta.append({
            "model": "basic.imagemeta",
            "pk": i + 1,
            "fields": {}
        })

        result_image_meta[j]['fields']['id'] = event['id']
        result_image_meta[j]['fields']['image_id'] = event['id']
        result_image_meta[j]['fields']['event_id'] = event['id']
        result_image_meta[j]['fields']['is_public'] = True
        result_image_meta[j]['fields']['description'] = 'Bitte einfügen.'
        result_image_meta[j]['fields']['is_open_source'] = True
        result_image_meta[j]['fields']['privacy_consent'] = True
        result_image_meta[j]['fields']['photographer_name'] = 'Robert'
        result_image_meta[j]['fields']['uploaded_at'] = event['created_at']


with open('output/image.json', 'w') as outfile:
    json.dump(result_image, outfile)

with open('output/image_meta.json', 'w') as outfile:
    json.dump(result_image_meta, outfile)
