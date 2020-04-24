import sys
import os
import glob
from PIL import Image


def read_cmd_args():
    try:
        source_folder = sys.argv[1]
        destination_folder = sys.argv[2]
        return source_folder, destination_folder
    except IndexError:
        print('Arguments are missing. Please try again and enter two arguments: source folder and destination folder. '
              'Exiting...')
        exit()


def get_image(folder):
    images = glob.glob(os.path.join(folder, '*.jpg'))
    if len(images) == 0:
        print('JPG images are not found in source folder. Exiting...')
        exit()
    else:
        for img_path in images:
            image_name = os.path.basename(img_path)
            image_clean_name = os.path.splitext(image_name)[0]
            yield image_clean_name, Image.open(img_path)


if __name__ == '__main__':

    source, destination = read_cmd_args()
    script_folder = os.path.dirname(os.path.abspath(__file__))

    path_source = os.path.join(script_folder, source)
    path_destination = os.path.join(script_folder, destination)

    if not os.path.exists(path_source):
        print('Source folder does not exist. Exiting...')
        exit()

    if not os.path.exists(path_destination):
        os.mkdir(destination)

    for img_name, img in get_image(path_source):
        img.save(os.path.join(destination, img_name + '.png'))







