#!/usr/bin/env python
#Author: Dustin Dodson
#Date modified: June 17, 2015

import urllib
import errno
import os

class Download:
    """This class is to be used to download files."""

    def __init__(self):
        self.baseDirectory = ""
        self.storeDirectory = ""

    def requireDirectory(self, path):
        try:
            os.makedirs(path)
            print 'Created new directory: %s' % (path)
        except OSError, exc:
            if exc.errno != errno.EEXIST:
                raise

    def downloadFile(self, url, filename):
        saveDir = ""
        if len(self.storeDirectory) == 0:
            saveDir = self.baseDirectory
        else:
            saveDir = self.storeDirectory

        self.requireDirectory(saveDir)
        if not os.path.exists(saveDir + filename):
            urllib.urlretrieve(url, (saveDir + filename))

    def setBaseDirectory(self, dir):
        self.baseDirectory = dir

    def setCreateNewDirectory(self, name):
        self.storeDirectory = (self.baseDirectory + name)
