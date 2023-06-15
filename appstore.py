import requests
import xmltodict
from datetime import datetime

# AppStore에서 Review 전체를 가져오는 함수
def appstore_crawler():
    f = open('app_last.txt', 'r')
    last_review_date = f.readline()
    last_review_date = datetime.fromisoformat(last_review_date)

    url = 'https://itunes.apple.com/kr/rss/customerreviews/page=1/id={your ios app id}/sortby=mostrecent/xml'
    results = []

    response = requests.get(url).content.decode('utf8')

    xml = xmltodict.parse(response)['feed']['entry']

    xml.sort(key=lambda x:x['updated'])

    for i in range(len(xml)):
        review_date = datetime.fromisoformat(xml[i]['updated'])
        print(review_date)
        if review_date > last_review_date:
            results.append({
                'USER': xml[i]['author']['name'],
                'DATE': xml[i]['updated'],
                'STAR': int(xml[i]['im:rating']),
                'TITLE': xml[i]['title'],
                'REVIEW': xml[i]['content'][0]['#text'],
                "LINK": xml[i]['link']['@href'],
                "TYPE": 'app'
            })
            last_review_date = review_date

    f = open('app_last.txt', 'w')
    f.write(datetime.isoformat(last_review_date))

    return results

def send_data(data):
    response = requests.get(
        url='{your destination to send data}',
        params=data
        )

if __name__ == '__main__':
    datas = appstore_crawler()
    for data in datas: 
        send_data(data)
