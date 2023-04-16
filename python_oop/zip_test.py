import os
import sys
import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    def __init__(self, zip_name):
        self.zip_name = zip_name
        self.temp_directory = Path("unzipped-{}".format(zip_name[:-4]))
        print(self.temp_directory)

    def process_zip(self):
        self.unzip_files()
        self.process_file()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zip_name) as zips:
            zips.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.zip_name, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_file(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open('w') as file:
                file.write(contents)


if __name__ == "__main__":
    test = ZipReplace('test.zip', 'has', 'is')
    test.process_zip()

