class StatsDirectoryGenerator:
    def get_links_for_year(self, year):
        pass

    def get_file_name_for_year(self, year):
        pass

    def get_directory_name(self):
        pass

    def get_table_class(self):
        pass

class BiosDirectoryGenerator(StatsDirectoryGenerator):
    def get_links_for_year(self, year):
        return [f"https://basketball.realgm.com/nba/players/{year}"]

    def get_file_name_for_year(self, year):
        return f'bios_{year}.csv'

    def get_directory_name(self):
        return "Bios"

    def get_table_class(self):
        return "tablesaw"
    
class TotalsDirectoryGenerator(StatsDirectoryGenerator):
    def get_links_for_year(self, year):
        return [f"https://basketball.realgm.com/nba/stats/{year}/Totals/All/points/All/desc/{page}/Regular_Season" for page in range(1, 10)] 

    def get_file_name_for_year(self, year):
        return f'totals_{year}.csv'

    def get_directory_name(self):
        return "Totals"

    def get_table_class(self):
        return "tablesaw"
    
class AverageDirectoryGenerator(StatsDirectoryGenerator):
    def get_links_for_year(self, year):
        return [f"https://basketball.realgm.com/nba/stats/{year}/Averages/All/points/All/desc/{page}/Regular_Season" for page in range(1, 10)] 

    def get_file_name_for_year(self, year):
        return f'averages_{year}.csv'

    def get_directory_name(self):
        return "Averages"

    def get_table_class(self):
        return "tablesaw"
    
class PerMinuteDirectoryGenerator(StatsDirectoryGenerator):
    def get_links_for_year(self, year):
        return [f"https://basketball.realgm.com/nba/stats/{year}/Per_Minute/All/points/All/desc/{page}/Regular_Season" for page in range(1, 10)] 

    def get_file_name_for_year(self, year):
        return f'per_minute_{year}.csv'

    def get_directory_name(self):
        return "PerMinute"

    def get_table_class(self):
        return "tablesaw"