'''
This downloads, and preprocesses scripts from the open movie script database.

written by: Dominik Kaukinen
'''
from downloader import *
import sys
import shutil
from utility import *

def main():
    for arg in sys.argv:
        if arg == "clean":
                shutil.rmtree('data')
                print "Removed temporary and data files, re-run to re-download..."
                return
    d = Downloader()
    d.download()
    if(deleteSmallFiles()):
        #TODO run preprocessor
    else:
        terminalContinue()

def terminalContinue():
    x = raw_input("Some failed downloads couldn't be deleted. Run preprocessor anyways? (y/n)")
    x = x.lower()
    if x == "y" or x == "yes":
        return True
    elif x == "n" or x == "no":
        return False
    else:
        print "Not valid respone\n"
        return terminalContinue()

if __name__=="__main__":
    main()
