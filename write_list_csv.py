import csv

def write_list_csv(list):
    with open('list.csv','w') as file:
        for l in list:
            file.write(l + '\n')
            return file