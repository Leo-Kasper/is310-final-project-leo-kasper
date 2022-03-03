import csv

def overall(row: list):
    count = 0
    for i in range(1, len(row)):
        count += int(row[i])
    return count

data_table = []

with open("tools_dh_proceedings.csv", "r") as input_file:
    csv_reader = csv.reader(input_file)
    for i, row in enumerate(csv_reader):
        data_table.append(row)
        if i == 0:
            data_table[i].append('Overall');
        else:
            data_table[i].append(overall(row))



for row in data_table:
    print(row[0], row[1], row[5], row[6], sep=' ', end='\n')

def printer(table: list, name: str):
    for row in table:
        for item in row:
            if item == name:
                print(*row, sep = ", ")
                return

printer(data_table, 'Python')


                     
                 
