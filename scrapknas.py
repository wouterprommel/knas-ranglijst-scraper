"""Scraper om Ranklijsten van Knas af te halen"""

import csv
from bs4 import BeautifulSoup
import requests


def save(to, content):
    with open(to, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        sort = 1

        # print("Rank,ID")
        writer.writerow(['Rank', 'ID'])

        for numbers in content.select('.number'):
            get = numbers.string

            if sort == 1:
                part1 = get

            elif sort == 2:
                part2 = get

            elif sort == 3:
                writer.writerow([part1, part2])

            elif sort == 4:
                sort = 0

            sort += 1


print("opgeslagen als Gender_Wapen_Categorie bijv. H_F_S.csv")
q1 = input("Alles (y/n)")
if (q1 == "y"):
    alles = True
elif (q1 == "n"):
    q2 = input("wapen: (F/E/S) ")
    q3 = input("gender: (M/F)")
    q4 = input("leeftijd cat (jeugd/senioren/veteranen): ")
else:
    print("enter (y/n)")
    raise SystemExit

with open("categorien.csv", "r") as categorien:
    for cat in categorien:
        line = cat.rstrip().split(',')
        parts = line[0].split('_')
        if (alles or True):
            response = requests.get(line[1], timeout=5)
            content = BeautifulSoup(response.content, "html.parser")
            line[0] += '.csv'
            save(line[0], content)
