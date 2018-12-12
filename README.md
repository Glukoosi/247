```
Flask app for requesting access to OTiT guild room.
Submitted form will go straight to Google Sheets.

Service account key and reCAPTCHA keys is needed from Google.
```


```
docker-compose up

or

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask run


for prod:
docker-compose -f docker-compose_prod.yml up -d
```

