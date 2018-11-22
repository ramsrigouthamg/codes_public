import requests

# https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
# https://gcloud-python.readthedocs.io/en/latest/storage/buckets.html

payload =    {"url" : "https://youtu.be/UzZFdEY4vJ0"}
url = "https://asia-northeast1-video-translation-219707.cloudfunctions.net/download_video"

r = requests.post(url,data=payload)
print ("Status Code ",r.status_code)

# r.ok returns True if status_code is less than 400, False if not
Status = "Success" if r.ok else "Failed"
print (Status)
