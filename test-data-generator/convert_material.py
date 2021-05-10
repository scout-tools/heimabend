import json

result_name = []
result_item = []
counter = 1

with open('input/event_dump.json') as json_file:
    events = json.load(json_file)

for i, event in enumerate(events, start=1):
    materials = event['material'].split(',')
    event_id = event['id']
    print(event_id)
    for material in materials:
        material = material.strip()
        if (len(material) < 3):
            continue
        counter += 1
        result_name.append({
            "model": "basic.materialname",
            "pk": counter,
            "fields": {
                "id": counter,
                "name": material[:29]
            }
        })

        result_item.append({
            "model": "basic.materialitem",
            "pk": counter,
            "fields": {
                "id": counter,
                "event_id": event_id,
                "quantity": 1,
                "material_name_id": counter,
                "material_unit_id": 1
            }
        })


with open('output/material_name.json', 'w') as outfile:
    json.dump(result_name, outfile)

with open('output/material_item.json', 'w') as outfile:
    json.dump(result_item, outfile)
