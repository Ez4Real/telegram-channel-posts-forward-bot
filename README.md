### 1. Clone repo from the link below
https://github.com/Ez4Real/telegram-channel-posts-forward-bot
### 2. Ensure that You have python 3.12.2 or newer on your machine. If You don't install it by link below
https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
### 3. Run package installation using сommand
`pip install -r requirements.txt`
### 4. Obtain Your api_id and api_hash by instruction in the link below, then write them into .env file created in root level of the project
https://core.telegram.org/api/obtaining_api_id

### 5. Run first `session_file_generate.py` script to generate your session file. 
`python session_file_generate.py`
### The script will ask you to enter the phone number linked to your Telegram account and confirm with code. 
Note that it is better not to change the name `telegram-session` in both scripts. If you change it in one of them, make sure that it is specified correctly in both.
### 6. Run your main telegram app (command below) and enjoy its working :)
`python main.py`

