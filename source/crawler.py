import sys
import urllib
import re
url = 'https://github.com/brada1/bmm/raw/master/downloads/'
parse_re = re.compile('href="([^"]*)".*(..-...-.... ..:..).*?(\d+[^\s<]*|-)')
          # look for          a link    +  a timestamp  + a size ('-' for dir)
def list_apache_dir(url):

    html = urllib.urlopen(url).read()

    files = parse_re.findall(html)
    dirs = []
    print (url + ' :' )
    print ('%4d file' % len(files) + 's' * (len(files) != 1))
    for name, date, size in files:
        if size.strip() == '-':
            size = 'dir'
        if name.endswith('/'):
            dirs += [name]
        print ('%5s  %s  %s' % (size, date, name))

    for dir in dirs:
        print
        list_apache_dir(url + dir)

for url in sys.argv[1:]:
    print
    list_apache_dir(url)
