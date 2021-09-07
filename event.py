from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

class Event(object):
    def __init__(self) -> None:
        self.dct = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

    def get_count_down(self, deadline):
        items = deadline.split()
        time = items[-3]
        hour, minute, second = list(map(int, time.split(":")))
        year = int(items[2])
        day = int(items[1][:-1])
        month = self.dct[items[0]]
        deadlineDate = datetime(year, month, day, hour, minute, second)
        now = datetime.now()
        duration = deadlineDate - now + timedelta(hours=7)
        hourl, minutel = duration.seconds//3600, (duration.seconds//60) % 60
        return str(duration.days) + " ngày " + str(hourl) + " giờ " + str(minutel) + " phút"

    def get_events(self):
        url = "https://genshin-impact.fandom.com/wiki/Events"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        tables = soup.find_all('table')
        children = tables[1].findChildren('a')
        names, links, times = [], [], []
        for item in children[1::2]:
            names.append(item.text)
            links.append(item['href'])
        for item in links:
            web = "https://genshin-impact.fandom.com" + item
            html = requests.get(web).text
            s = BeautifulSoup(html, "lxml")
            times.append(s.find('span', {'class': 'countdowndate'}).text)
        countdowns = [self.get_count_down(deadline) for deadline in times]
        return names, links, countdowns