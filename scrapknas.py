"""Scraper om Ranklijsten van Knas af te halen"""

import sys
import csv
from bs4 import BeautifulSoup
import requests


def save(to, content):
    with open("rank/" + to, mode='w') as csv_file:
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


def check_file(use_file):
    parts = use_file.split('.')
    if len(parts) == 2 and parts[1] == "csv":
        return True
    else:
        run_help()
        return False


def run_help():
    print("HELP")
    print("Gebruik: python scrapknas.py 'filename.csv'")
    print("De 'filenames' zijn te vinde in het mapje categorien")
    print("De ranklijsten worden opgeslagen als Gender_Wapen_Categorie bijv. H_F_S.csv")
    exit()


if len(sys.argv) == 2:
    use_file = sys.argv[1]
else:
    run_help()

if check_file(use_file):
    with open("categorien/" + use_file, "r") as categorien:
        for cat in categorien:
            line = cat.rstrip().split(',')
            parts = line[0].split('_')
            response = requests.get(line[1], timeout=5)
            content = BeautifulSoup(response.content, "html.parser")
            line[0] += '.csv'
            save(line[0], content)
