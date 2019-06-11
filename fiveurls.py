#!/usr/bin/python3

import webbrowser
import time

data=input("Search here:")
webbrowser.open_new_tab("https://www.google.com/search?q="+data)

x=["https://en.wikipedia.org/wiki/hello_(adele_song)","https://hello.com/","https://supersimple.com/song/hello/","https://www.hellomagazine.com/","https://en.oxfordictionaries.com/definitions/hello/"]
for i in range(0,5):
	webbrowser.open_new_tab(x[i])
	i = i+1
	time.sleep(5)

