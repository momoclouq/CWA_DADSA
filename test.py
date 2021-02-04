import csv



    with open('shoplist.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row['NAME'])



