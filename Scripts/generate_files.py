import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from StatsDirectoryGenerators import StatsDirectoryGenerator, BiosDirectoryGenerator, TotalsDirectoryGenerator, AverageDirectoryGenerator, PerMinuteDirectoryGenerator

YEAR_FROM = 2000
YEAR_TO = 2023

def make_sure_directory_exists(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

"""def get_bios_csv_files():
    def get_bios_for_season_link(year):
        return f"https://basketball.realgm.com/nba/players/{year}"

    for year in range(YEAR_FROM, YEAR_TO+1):
        URL = get_bios_for_season_link(year)
        resp = requests.get(URL)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            tab = soup.find('table', {"class": "tablesaw"})
            df = pd.read_html(str(tab))[0]
            make_sure_directory_exists("Bios")
            file_path = os.path.join("Bios", f'bios_{year}.csv')
            df.to_csv(file_path, index=False)"""

def generate_csv_files(directory_generator: StatsDirectoryGenerator):
    for year in range(YEAR_FROM, YEAR_TO+1):
        URLs = directory_generator.get_links_for_year(year)
        num_of_url = 0
        for URL in URLs:
            resp = requests.get(URL)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                tab = soup.find('table', {"class": directory_generator.get_table_class()})
                if tab:
                    df = pd.read_html(str(tab))[0]
                    dir_name = directory_generator.get_directory_name()
                    make_sure_directory_exists(dir_name)
                    file_path = os.path.join(dir_name, directory_generator.get_file_name_for_year(year))
                    #df.to_csv(file_path, mode={'w' if num_of_url == 0 else 'a'}, header={num_of_url == 0}, index=False)
                    if num_of_url == 0:
                        df.to_csv(file_path, mode='w', header=True, index=False)
                    else:
                        df.to_csv(file_path, mode='a', header=False, index=False)
                    num_of_url += 1

"""dir_generators = [BiosDirectoryGenerator(), TotalsDirectoryGenerator(), AverageDirectoryGenerator(), PerMinuteDirectoryGenerator()]
for dir_generator in dir_generators:
    generate_csv_files(dir_generator)"""

dir_generators = [AverageDirectoryGenerator()]
for dir_generator in dir_generators:
    generate_csv_files(dir_generator)