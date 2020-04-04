import csv
import re
import pymongo
from pymongo import MongoClient
client = MongoClient()
My_db = client['music']
concerts = My_db['concerts']


def read_data(csv_file, db):
    list_of_data = []
    with open(csv_file, encoding='utf-8', newline="") as datafile:
        flats_csv = csv.DictReader(datafile, delimiter=",")
        for one in flats_csv:
            list_of_data.append(one)
    insert = db.insert_many(list_of_data)


def find_cheapest(db):
    for item in db.find().sort('Цена', pymongo.ASCENDING):
        print(item)

def find_by_name(db, name=input('Введите имя исполнителя: ')):
    pattern = re.compile(f"[а-яА-Яa-zA-z0-9]*{name}[а-яА-Яa-zA-z0-9]*")
    for item in db.find():
        text_cor = re.search(pattern, str(item))
        if text_cor is not None:
            print(item)

if __name__ == '__main__':

    find_by_name(concerts)
    # read_data('artists.csv', concerts)
    # find_cheapest(artists)
    # for item in concerts.find():
    #     print(item)

