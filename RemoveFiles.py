import os
import shutil
import time

def main():
    path = 'Documents'
    days = 30
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for rootFolders, folders, files in os.walk(path):
            if seconds>=getFileOrFolderAge(rootFolders):
                removeFolders(rootFolders)
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolders, folder)
                    if seconds>=getFileOrFolderAge(folderPath):
                        removeFolders(folderPath)
                for file in files:
                    filePath = os.path.join(rootFolders, file)
                    if seconds>= getFileOrFolderAge(filePath):
                        removeFiles(filePath)
    else:
        print('path not found')


def getFileOrFolderAge(path):
    ageFile = os.stat(path).st_ageFile
    return ageFile

def removeFolders(path):
    if not shutil.rmtree(path):
        print('path removed sucessfully')
    else:
        print('cannot delete file')

def removeFiles(path):
    if not os.remove(path):
        print('path removed sucessfully')
    else:
        print('cannot delete file')

main()
