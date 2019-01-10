import urllib

captcha = "2a12359e"

while True:
    x = urllib.urlopen("http://ctf.slothparadise.com/walled_garden.php?name=sashank&captcha=" + captcha).read()
    if "KEY" in x:
        print x
        break
    b=x.split("<pre>")
    c=b[1].split("</pre>")
    d=c[0]
    captcha = d.decode("ascii")
