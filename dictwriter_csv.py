import csv
import os.path

def write_csv(book):
    with open('book_info.csv', mode='a+', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=book.keys(), delimiter=",", lineterminator = "\n")
        if os.path.getsize('book_info.csv') == 0:
             writer.writeheader()
        writer.writerow(book)
    return file
                