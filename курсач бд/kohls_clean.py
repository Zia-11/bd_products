import json

with open('data/kohls.json', 'r') as file:
    data = json.load(file)

products = data.get('payload', {}).get('products', [])

extracted_data = []
for product in products:
    item = {
        'name': product.get('productTitle'),
        'price': product.get('prices', [{}])[0].get('regularPrice', {}).get('minPrice'),
        'url': f"https://www.kohls.com{product.get('seoURL')}",
        'image': product.get('image', {}).get('url')
    }
    extracted_data.append(item)

with open('data/kohls_cleaned.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)
