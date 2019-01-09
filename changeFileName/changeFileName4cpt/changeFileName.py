import os
import re


def replaceDirName(rootDir):
    dirs = os.listdir(rootDir)

    for dir in dirs:
        # oldname = dir.split('&')
        # newname = oldname[0] + '_' + oldname[1]
        #
        # oldpath = os.path.join(rootDir, dir)
        # newpath = os.path.join(rootDir, newname)
        #
        # os.rename(oldpath, newpath)
        print(dir)



if __name__ == '__main__':
    rootDir = 'D:\\IDEAProjects\\cptiscas\\src\\main\\java\\mutants'
    replaceDirName(rootDir)
