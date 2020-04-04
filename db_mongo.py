import csv
import re
import pymongo
from pymongo import MongoClient
client = MongoClient()
My_db = client['music']
concert = My_db['concert']


def read_data(csv_file, db):
    list_of_data = []
    with open(csv_file, encoding='utf-8', newline="") as datafile:
        flats_csv = csv.DictReader(datafile, delimiter=",")
        for one in flats_csv:
            one['Цена'] = int(one['Цена'])
            list_of_data.append(one)
    insert = db.insert_many(list_of_data)
    for item in db.find():
        print(item)


def find_cheapest(db):
    for item in db.find().sort('Цена', pymongo.ASCENDING):
        print(item)

def find_by_name(db, name=input('Введите имя исполнителя: ')):
    pattern = re.compile(f"[а-яА-Яa-zA-z0-9]*{name}[а-яА-Яa-zA-z0-9]*")
    result = list(db.find({'Исполнитель': pattern}))
    print(result)

if __name__ == '__main__':

    find_by_name(concert)
    # read_data('artists.csv', concert)
    find_cheapest(concert)
    # for item in concerts.find():
    #     print(item)
