import time
from datetime import datetime as dt

hosts_path_win = "C:\Windows\System32\drivers\etc\hosts"
host_temp = "hosts"

redirect = "127.0.0.1"

websites_list = [
    "https://www2.hm.com/da_dk/index.html",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.dba.dk/"
    "https://web.whatsapp.com/"  
]

from_hour = 6
to_hour = 17

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("working time")
        with open(hosts_path_win, 'r+') as file:
           content = file.read()
           for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n" )
           print(content)
    else:
        print("fun time")
        with open(hosts_path_win, 'r+') as file:
           content = file.readlines()
           file.seek(0)
           for line in content:
            if not any(website in line for website in websites_list):
                file.write(line)
            file.truncate()