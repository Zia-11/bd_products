import json

with open('data/HM.json', 'r') as file:
    data = json.load(file)

products = data.get('results', [])

extracted_data = []
for product in products:
    item = {
        'name': product.get('name'),
        'price': product.get('price', {}).get('value'),
        'url': f"https://www2.hm.com{product.get('linkPdp')}",
        'image': product.get('images', [{}])[0].get('url')
    }
    extracted_data.append(item)

with open('data/HM_cleaned.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)

