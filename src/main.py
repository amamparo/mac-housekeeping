import os
import pwd

from crontab import CronTab


def __move_older_than_to_trash(days_old: int, _dir: str) -> str:
    return 'find %s -type f -atime +%s -exec mv -f {} ~/.Trash \\;' % (
        _dir,
        days_old
    )


def __clean_desktop(cron: CronTab) -> CronTab:
    job = cron.new(
        command=__move_older_than_to_trash(1, '~/Desktop'),
        comment='Move desktop files older than 1 day to trash'
    )
    job.every(1).hours()
    return cron


def __clean_downloads(cron: CronTab) -> CronTab:
    job = cron.new(
        command=__move_older_than_to_trash(1, '~/Downloads'),
        comment='Move download files older than 1 day to trash'
    )
    job.every(1).hours()
    return cron


def __empty_trash(cron: CronTab) -> CronTab:
    job = cron.new(
        command='find ~/.Trash -type f -atime +7d -exec rm -rf {} \\;',
        comment='Empty trash of all items older than 1 week'
    )
    job.every(1).hours()
    return cron


def main():
    username = pwd.getpwuid(os.getuid())[0]
    with CronTab(user=username) as cron:
        cron.remove_all()
        __clean_desktop(cron)
        __clean_downloads(cron)
        __empty_trash(cron)
        cron.write()


if __name__ == '__main__':
    main()
