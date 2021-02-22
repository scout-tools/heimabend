import json

model = "basic.tag"

result = []

with open('input/tag-category.json') as json_file:
    tag_category_obj = json.load(json_file)

with open('input/tags.json') as json_file:
    tags_obj = json.load(json_file)

for i, event in enumerate(tags_obj, start=1):
    result.append({
        "model": model,
        "pk": i,
        "fields": {}
    })

    result[i-1]['fields']['id'] = event['id']
    result[i-1]['fields']['name'] = event['name']
    result[i-1]['fields']['description'] = event['description']
    result[i-1]['fields']['color'] = event['color']
    result[i-1]['fields']['category_id'] = int(event['category'].split("/")[5])

with open('output/tags.json', 'w') as outfile:
    json.dump(result, outfile)
