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
                    if num_of_url == 0:
                        df.to_csv(file_path, mode='w', header=True, index=False)
                    else:
                        df.to_csv(file_path, mode='a', header=False, index=False)
                    num_of_url += 1

dir_generators = [BiosDirectoryGenerator(), TotalsDirectoryGenerator(), AverageDirectoryGenerator(), PerMinuteDirectoryGenerator()]
for dir_generator in dir_generators:
    generate_csv_files(dir_generator)