from skimage.io import imread, imsave, imshow, show
import matplotlib.pyplot as plt
import pynder
from helpers import get_access_token, get_login_credentials
from io_helper import save_image

email, password, FBID = get_login_credentials()
FBTOKEN = get_access_token(email, password)
session = pynder.Session(facebook_token=FBTOKEN)

while True:
    users = session.nearby_users()
    for user in users:
        photos = user.get_photos()
        print("Fetched user photos..")
        for photo in photos:
            print(photo)
            image = imread(photo)
            imshow(image)
            show()

            input_string = "Write 1 to like. Write 2 to dislike."
            ans = str(input(input_string)).lower()

            if ans == "1":
                save_image(image, photo, True)
            else:
                save_image(image, photo, False)
