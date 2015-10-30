'''
Some miscellaneous functions here to be used for utility
'''
import os

'''
This functions deletes files < 50kb.
This is to prevent failed script downloads from being
included in the training data.

returns True or False dending on if successful or not
'''
def deleteSmallFiles():
    fileList = os.listdir(tempHtmlDirectory)
    for f in fileList:
        if os.path.getsize(f) < 15000:
        try:
            os.remove(f)
        except IOError:
            print "Unable to delete " + f + " check to make sure it isn't open."
            return False
    return True
