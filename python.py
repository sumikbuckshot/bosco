#!/usr/bin/python3

import webbrowser
import time
import subprocess
option='''
Press 1 to start your vlc:
Press 2 to start your fav song on youtube:
Press 3 to search something on google:
Press 4 to send whatsapp msg:
Press 5 to check current time and date:
Press 6 to reboot your machine
'''
print(option)
choice=int(input())
if choice==5:
	current_time=time.ctime()
	print(current_time)
elif choice==1:
	subprocess.getoutput('vlc')
elif choice==3:
	data=input('what do you wanna search:')
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)
elif choice==2:
	data1=input("which song on youtube:")
	webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+data1)
elif choice==4:
	driver=webdriver.chrome('/home/adhoc/Desktop/chromedriver')
	driver.get("https://web.whatsapp.com/")
	wait=WebDriverWait(driver,600)
	target='Priyanshu'
	string='lodu'

else :
	print('cant help you')
