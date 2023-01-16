import pandas as pd
import os

#read_html function to extract tables from an url
url = input("Insira a URL/Insert the URL: ")
tables = pd.read_html(url)
#access first table (planilha)
table = tables[0]
#save into csv
table.to_csv('table.csv', index=False)
# Get the current working directory
cwd = os.getcwd()
# Join the current working directory with the filename
file_path = os.path.join(cwd, 'table.csv')
print("Arquivo criado em/Created in: ",file_path)