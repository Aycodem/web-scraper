import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text , 'html.parser')

table = soup.find('table', class_='wikitable sortable')

world_titles=table.find_all('th')
world_table_title=[title.text.strip() for title in world_titles]

df =pd.DataFrame(columns=world_table_title)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length]=individual_data

df.to_csv('companies.csv', index=False)