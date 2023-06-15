from google_play_scraper import app, Sort, reviews_all
from datetime import datetime
import requests

def get_play_reviews():
    f = open('play_last.txt', 'r')
    last_review_date = f.readline()
    last_review_date = datetime.strptime(last_review_date, '%Y-%m-%d %H:%M:%S')

    ko_reviews = reviews_all(
        '{your google app id}',
        sleep_milliseconds=0, # defaults to 0
        lang='ko', # defaults to 'en'
        country='kr', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    )

    results = []
    ko_reviews.reverse()
    for review in ko_reviews:
        review_date = review['at']
        print(review_date)
        if last_review_date < review_date:
            result = {
                    'USER': review['userName'],
                    'DATE': review['at'].strftime("%Y-%m-%d %H:%M:%S"),
                    'STAR': review['score'],
                    'TITLE': '',
                    'REVIEW': review['content'],
                    "LINK": '',
                    "TYPE": 'play'
                }
            results.append(result)
            last_review_date =  review_date
    
    f = open('play_last.txt', 'w')
    f.write(last_review_date.strftime('%Y-%m-%d %H:%M:%S'))
    return results

def send_data(data):
    response = requests.get(
        url='${your destination to send data}',
        params=data
        )
    
if __name__ == "__main__":
    datas = get_play_reviews()
    for data in datas:
        send_data(data)