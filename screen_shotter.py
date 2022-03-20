from PIL import ImageGrab
from threading import Thread

import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None' 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time, os, pyperclip

def plt_show(im:ImageGrab, image_name:str) -> None:
    """
    Image function which gets multithreaded.
    :param im: Object of type ImageGrab.
    :param image_name: str denoting the image path name.
    """
    im.save(image_name,'PNG')
    pyperclip.copy('')  # Clears in case of prior runs.
    img = mpimg.imread(image_name)
    os.remove(image_name)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

image_name, previous_screen_shot_id = 'screen_shotter_image.png', 0
while True:
    try:
        im = ImageGrab.grabclipboard()
        if im is not None and type(im) != list: # Trigger if the clip board isn't empty and that only a single image is copied.
            current_screen_shot_id = id(im)
            if current_screen_shot_id != previous_screen_shot_id:
                previous_screen_shot_id = current_screen_shot_id
                new_thread = Thread(target=plt_show,args=(im, image_name))
                new_thread.start()
    except OSError as e:
        print('Suppressing error [' + str(e) + ']')
    finally:
        time.sleep(1)