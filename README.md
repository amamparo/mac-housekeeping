# Who is this for?
A mac user who would like to keep their desktop, downloads, and trash de-cluttered.

# What does it do?
This python script initializes the following hourly cleanup tasks
- Move files in ~/Desktop that haven't been accessed in over 1 day to trash
- Move files in ~/Downloads that haven't been accessed in over 1 day to trash
- Empty trash of all files that haven't been accessed in over 1 week

# Requirements
- Python 3.8.x
- [pipenv](https://pypi.org/project/pipenv/)

# How to use it
Just run `make cron`

> **⚠ WARNING**: This will clear out all existing cron jobs before running, so do not run this unless your crontab file is empty or you don't care about keeping its current contents.