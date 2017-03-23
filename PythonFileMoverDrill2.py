


# Python Version: 2.7.13
# Author: Gavin Bramley
# Python Drill 3, moving files based on date modified

import os, time, shutil


def filecopy(src, dst):
    now = time.time()  # gets current time
    docs = os.listdir(src) # searches source folder for documents in it .txt files that were created
    for i in docs:
        x = src + '\\' + i # gets complete file path from the folder with the documents
        modtime = os.stat(x).st_mtime # reads the last modified date of each file
        past24 = (now - 86400)  # gets time of last 24 hrs in sec
        if modtime > past24:  # compares the last modified time vs 24 hours ago
            shutil.copy(x, dst) # copies file that were modified within last 24 hours
            print x


def main():
    folder_src = 'C:\\miniconda3\\pythondatetime\\folderA'
    folder_dest = 'C:\\miniconda3\\pythondatetime\\folderB'
    filecopy(folder_src, folder_dest)

if __name__ == "__main__":
    main()