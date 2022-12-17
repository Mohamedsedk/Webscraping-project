from bs4 import BeautifulSoup
import requests

url = 'https://www.reddit.com/search/?q=python'

the_web = requests.get(url)
source = the_web.content
elements = BeautifulSoup(source, "html.parser")
links = elements.find_all("a", {"class": "SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
timestamp = elements.find_all("span", {"class": "_2VF2J19pUIMSLJFky-7PEI"})
posts = elements.find_all("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
activities = elements.find_all("div", {"class": "_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"})
poster_ = []
link_ = []
time_ = []
post_ = []
activity_ = []
for i in range(len(timestamp)):
    time_.append(timestamp[i].text)
    post_.append(posts[i].text)
    link_.append(links[i].attrs["href"])
    activity_.append(activities[i].text.replace("s", "s   |  ")[:-3])
for link1 in link_:
    link_split = str(link1).split('/')
    poster_.append(link_split[2])

for i in range(len(poster_)):
    print(poster_[i] + " >>", post_[i] + " >> ", time_[i] + " >> ", activity_[i])
    print('\n')
