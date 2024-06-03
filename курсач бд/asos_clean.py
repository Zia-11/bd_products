import json

with open('data/asos.json', 'r') as file:
    data = json.load(file)

products = data.get('products', [])

extracted_data = []
for product in products:
    item = {
        'name': product.get('name'),
        'price': product.get('price', {}).get('current', {}).get('value'),
        'url': f"https://www.asos.com/{product.get('url')}",
        'image': f"https://{product.get('imageUrl')}"
    }
    extracted_data.append(item)

with open('data/asos_cleaned.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)

