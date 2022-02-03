import os

script_dir = os.path.dirname(__file__)
photo_path = os.path.join(script_dir, 'pics/temp_image.jpg')

def takePicture():
    os.system("fswebcam -r 1280x720 --no-banner {}".format(photo_path))
    print("temporary picture taken")

def deletePicture():
    os.system("rm -rf {}".format(photo_path))
    print("temporary picture deleted")

if __name__=="__main__":
    script_dir = os.path.dirname(__file__)
    photo_path = os.path.join(script_dir, 'pics/temp_image.jpg')
    takePicture()
    print(photo_path)