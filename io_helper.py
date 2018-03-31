from skimage.io import imsave

base_folder = "validation"

def save_image(image, name, liked):

    filename = base_folder

    if liked:
        filename += "/likes/"
    else:
        filename += "/dislikes/"

    file_url_list = name.split("/")
    filename += file_url_list[-1]
    print(filename)
    imsave(filename, image)
