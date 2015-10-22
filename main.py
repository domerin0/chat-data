'''
This downloads, and preprocesses scripts from the open movie script database.

written by: Dominik Kaukinen
'''


from downloader import *
import sys

def main():
    d = Downloader()
    d.download()        

if __name__=="__main__":
    main()
