'''
This downloads, and preprocesses scripts from the open movie script database.

written by: Dominik Kaukinen
'''


from downloader import *
import sys
import shutil

def main():
    for arg in sys.argv:
        if arg == "clean":
                shutil.rmtree('data')
                print "Removed temporary and data files, re-run to re-download..."
                return
    d = Downloader()
    d.download()

if __name__=="__main__":
    main()
