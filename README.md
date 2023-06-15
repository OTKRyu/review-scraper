# Simple app review scraper

## requirements

```
# Both files are used for recording last review date
# This scraper will get only newer review than review date in those files
touch app_last.txt
touch play_last.txt
```

## install(window)

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## explanation

This scraper is just for app store review scraping and google play store review scraping.

I used to send scraped data to google spreadsheets so other people can see.
If you want to do so, you have to make your one spreadsheets and it's script to receive review data.

If you want to do this daily, then you can use window scheduler.
After Simple configuration, you can automate getting reviews.
