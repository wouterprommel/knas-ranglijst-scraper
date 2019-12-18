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

categories = {'D_F_S': 'https://knas.onzeranglijsten.net/pag/8094/rls/6844',
              'D_F_K': 'https://knas.onzeranglijsten.net/pag/8094/rls/b645',
              'D_F_B': 'https://knas.onzeranglijsten.net/pag/8094/rls/cb42',
              'D_F_P': 'https://knas.onzeranglijsten.net/pag/8094/rls/1943',
              'D_F_C': 'https://knas.onzeranglijsten.net/pag/8094/rls/ae40',
              'D_F_J': 'https://knas.onzeranglijsten.net/pag/8094/rls/fc41',
              'H_F_S': 'https://knas.onzeranglijsten.net/pag/8094/rls/3171',
              'H_F_K': 'https://knas.onzeranglijsten.net/pag/8094/rls/ac7e',
              'H_F_B': 'https://knas.onzeranglijsten.net/pag/8094/rls/fb7f',
              'H_F_P': 'https://knas.onzeranglijsten.net/pag/8094/rls/107c',
              'H_F_C': 'https://knas.onzeranglijsten.net/pag/8094/rls/5e7d',
              'H_F_J': 'https://knas.onzeranglijsten.net/pag/8094/rls/f37a'}

#  save_to = input("Oplaan als: ")
for cat in categories:
    response = requests.get(categories[cat], timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    cat += '.csv'
    save(cat, content)
