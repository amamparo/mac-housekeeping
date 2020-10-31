# What it is
A python script that specifies the following hourly cron jobs for the current-logged-in mac user:

- Move files in ~/Desktop that haven't been accessed in over 1 day to trash
- Move files in ~/Downloads that haven't been accessed in over 1 day to trash
- Empty trash of all files that haven't been accessed in over 1 week

# Requirements
- Python 3.8.x
- [pipenv](https://pypi.org/project/pipenv/)

# How to use it
Just run `make cron`

> **⚠ WARNING**: This will clear out all existing cron jobs before running, so do not run this unless your crontab file is empty or you don't care about keeping its current contents.