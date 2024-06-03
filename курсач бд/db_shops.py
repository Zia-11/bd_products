import json
import psycopg2

conn = psycopg2.connect(
    dbname="shops",
    user="postgres",
    password="1111",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def insert_data(file_path, table_name):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    for item in data:
        cursor.execute(
            f"""
            INSERT INTO {table_name} (name, price, url, image)
            VALUES (%s, %s, %s, %s)
            """,
            (item['name'], item['price'], item['url'], item['image'])
        )

insert_data('data/kohls_cleaned.json', 'kohls_table')
insert_data('data/HM_cleaned.json', 'hm_table')
insert_data('data/asos_cleaned.json', 'asos_table')

conn.commit()
cursor.close()
conn.close()
