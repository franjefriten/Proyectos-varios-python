import json
import pygal
import requests
from operator import itemgetter

def printdic(dic):
    print("\n")
    for key, value in dic.items():
        print(str(key) + ": " + str(value))

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
file =  requests.get(url)
print(file.status_code)

# Submissions
source = file.json()
submissions_dic = []
for elem in source[:30]:
    url2 = "https://hacker-news.firebaseio.com/v0/item/" + str(elem) + ".json"
    print(url2)
    file2 = requests.get(url2)
    print(file2.status_code)
    source2 = file2.json()
    printdic(source2)

    submission = {
        'title': source2['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(elem),
        'comments': source2.get('descendants', 0)
    }
    submissions_dic.append(submission)
    submissions_dic = sorted(submissions_dic, key=itemgetter('comments'), reverse=True)

for submission_dict in submissions_dic:    
    print("\nTitle:", submission_dict['title'])    
    print("Discussion link:", submission_dict['link'])    
    print("Comments:", submission_dict['comments'])