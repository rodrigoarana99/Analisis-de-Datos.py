import tabulate
import csv 

with open('regular.csv', 'r') as file:
    reader = csv.reader(file)
    table = list(reader)
    print(tabulate.tabulate(table, tablefmt='grid'))