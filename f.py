from instagrapi import Client
import time

client = Client()

username = 'username'
password = 'password'
client.login(username, password)

photo_path = '1.jpg'
caption = ''

while True:
    client.photo_upload(photo_path, caption)
    print(f"{time.ctime()}: Done!")

    time.sleep(10)  
