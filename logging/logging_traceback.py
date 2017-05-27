# https://stackoverflow.com/questions/1508467/log-exception-with-traceback
# Use logging.exception() to raise "traceback"

import logging
LOG_FILENAME = 'ogging_example.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

logging.debug('This message should go to the log file')

try:
    run_my_stuff()
except:
    logging.exception('Got exception on main handler')
    raise
