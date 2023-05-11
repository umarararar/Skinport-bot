import requests
import csv

api_key = 'G9jk4AyXca3zJvhA7FibR/wa88E9Atcp8mdqsdv0vBfwUdTLLDtwC0zkzg9AYuGAoEsc/Yq7b8+zrKekRgZHFA=='
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

response = requests.get('https://api.skinport.com/v1/items/', headers=headers)

if response.status_code == 200:
    data = response.json()
    sorted_data = sorted(data, key=lambda x: x['suggested_price'] if x['suggested_price'] is not None else float('inf'))
    # open csv file for writing
    with open('skinport_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # create csv writer
        writer = csv.writer(csvfile)
        # write header row
        writer.writerow(['Name', 'Suggested Price', 'Min Price', 'Max Price','Currency', 'Item Page                     '])
        # loop over items and write to csv
        for item in sorted_data:
            writer.writerow([item['market_hash_name'], item['suggested_price'], item['min_price'], item['max_price'], item['currency'], item['item_page']])
else:
    print(f'Error retrieving data from Skinport API: {response.status_code}')




