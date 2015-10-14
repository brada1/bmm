import urllib.request
import os, shutil

class Downloader():

    def dirExistCheck(d):
        # create download directory if it doesn't exist
        if  not os.path.isdir(d):
            print (d + " doesn't exist. Creating it...")
            os.makedirs(d)

    def dl(url, dld):
        # this is a simple downloader function
        Downloader.dirExistCheck(dld)

        # create the full target directory + filename path
        file_name =  dld + '\\' + url.split('/')[-1]
        
        # download
        print ("downloading " + url + " to " + dld + '...')
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print ('done')

    def rm(url, dld):
        # delete a given file path
        path = dld + '\\' + url.split('/')[-1]
        print ('removing ' + path + '...')
        os.remove(path)
        print ('done')
        
