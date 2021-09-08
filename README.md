# Kajot interview test
- This script is make to compress files to gzip files. Script is running automatically at 01:00 AM, every 30 days. Automation is handle by cron job.

# How to use
- Open Terminal and type here: `crontab -e`
    after that vim editor will open.
- Select `I` on keyboard to go to Insert mode
- Copy and paste this command to editor `0 1 */30 * * /path/to/python /path/to/script/file.py`
- Then press esc and write `:wq` to exit and save cron job
- ALL DONE!
