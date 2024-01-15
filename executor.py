import pystray
from PIL import Image
from pathlib import Path
import threading
import AppTrack


STATE = None


class IconError(Exception):
    def __init__(self, message=None):
        self.message = message
    

    def __str__(self):
        if self.message == None:
            return 'Icon pictures not found! Make sure that the paths are correct in the main() function!'
        return self.message


def execute(images):
    global STATE
    if STATE == None:
        run(images[0], 'AppTrack')
    elif STATE == 'Running':
        run(images[1], 'AppTrack (Running)')
    elif STATE == 'Halt':
        run(images[2], 'AppTrack (Halt)')
    

def run(img, tit):
    icon = pystray.Icon('AppTrack', icon=img, title=tit, menu=pystray.Menu(
        pystray.MenuItem('Run', order),
        pystray.MenuItem('Halt', order),
        pystray.MenuItem('Exit', order)
    ))
    icon.run()   


def order(icon, item):
    global STATE
    if str(item) == 'Run':
        
        STATE = 'Running'
        icon.stop()
        
    if str(item) == 'Halt':
        
        STATE = 'Halt'
        icon.stop()
    
    if str(item) == 'Exit':
        
        STATE = 'Exit'
        icon.stop()
        

def main():
    global STATE
    STATE = 'Running'
    try:
        image_default = Image.open(Path('d:/Marek/New_programming/Study/AppTrack/icon.png'))
        image_run = Image.open(Path('d:/Marek/New_programming/Study/AppTrack/icon_run2.png'))
        image_stop = Image.open(Path('d:/Marek/New_programming/Study/AppTrack/icon_stop.png'))
        images = [image_default, image_run, image_stop]
    except:
        raise IconError

    

    AppTrack.SIGNAL = STATE
    threading.Thread(target=AppTrack.track).start()

    while STATE != 'Exit':
        execute(images)
        print(STATE)
        AppTrack.SIGNAL = STATE



if __name__=='__main__':
    main()




