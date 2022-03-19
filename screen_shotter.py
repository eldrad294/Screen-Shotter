from PIL import ImageGrab
from threading import Thread

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time, os

def plt_show(im:ImageGrab, image_name:str) -> None:
    """
    Image function which gets multithreaded.
    :param im: Object of type ImageGrab.
    :param image_name: str denoting the image path name.
    """
    im.save(image_name,'PNG')
    img = mpimg.imread(image_name)
    os.remove(image_name)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.imshow(img)
    plt.axis('off')
    plt.show()

image_name, previous_screen_shot_id = 'screen_shotter_image.png', 0
while True:
    im = ImageGrab.grabclipboard()
    if im is not None:
        current_screen_shot_id = id(im)
        if current_screen_shot_id != previous_screen_shot_id:
            previous_screen_shot_id = current_screen_shot_id
            new_thread = Thread(target=plt_show,args=(im, image_name))
            new_thread.start()
    time.sleep(5)