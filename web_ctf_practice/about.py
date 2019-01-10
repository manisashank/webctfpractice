import urllib
KEY = "8000"

url="http://ctf.slothparadise.com/about.php"
while True:
    x = urllib.urlopen(url).read()
    if KEY in x:
        print x
        break

