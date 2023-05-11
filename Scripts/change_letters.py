import sys
import chardet

LETTERS_REPLACEMENTS = {
    'Ş': 'S',
    'ş': 's',
    'Š': 'S',
    'š': 's',
    'Ć': 'C',
    'ć': 'c',
    'Ö': 'O',
    'ö': 'o',
    'Ā': 'A',
    'ā': 'a',
    'Č': 'C',
    'č': 'c',
    'Ū': 'U',
    'ū': 'u',
    'Ó': 'O',
    'ó': 'o',
    'Ņ': 'N',
    'ņ': 'n',
    'Ģ': 'G',
    'ģ': 'g',
    'É': 'E',
    'é': 'e',
    'Ü': 'U',
    'ü': 'u',
}

PLAYERS_REPLACEMENTS = {
    "A.J. Green": "AJ Green",
    "Jeff Dowtin": "Jeff Dowtin Jr.",
    "John Butler": "John Butler Jr.",
    "Kevin Knox": "Kevin Knox II",
    "Marcus Morris": "Marcus Morris Sr.",
    "OG Anunoby": "O.G. Anunoby",
    "Robert Williams": "Robert Williams III",
    "Xavier Tillman Sr.": "Xavier Tillman"
}

class LettersReplacer:
    def __init__(self, filepath, replacements):
        self.filepath = filepath
        self.replacements = replacements

    def detect_encoding(self):
        with open(self.filepath, 'rb') as file:
            self.encoding = chardet.detect(file.read())['encoding']

    def read_from_file(self):
        with open(self.filepath, 'r', encoding=self.encoding) as file:
            self.contents = file.read()

    def perform_replacement(self):
        for key, value in self.replacements.items():
            self.contents = self.contents.replace(key, value)

    def save_replacements(self):
        with open(self.filepath, 'w', encoding=self.encoding) as file:
            file.write(self.contents)

    def replace(self):
        self.detect_encoding()
        self.read_from_file()
        self.perform_replacement()
        self.save_replacements()

if __name__ == "__main__":
    REPLACEMENTS = {**LETTERS_REPLACEMENTS, **PLAYERS_REPLACEMENTS}
    replacer = LettersReplacer(sys.argv[1], REPLACEMENTS)
    replacer.replace()
