

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### The Hard Way

```sh
virtualenv -p python3 VENV
. ./VENV/bin/activate
pip install -r requirements.txt
cp sample_config.py config.py
--- EDIT config.py values appropriately ---
python bot.py
```


#### LICENSE
- GPLv3
