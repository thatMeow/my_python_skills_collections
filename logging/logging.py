# -*- coding: utf-8 -*-
"""
@author: fiq831
"""
import logging

def setup_logging(file):
    """
    Stream handlers are commented out. If required, uncomment the lines that start
    with shandler and adding the same to logger. 
    """
    logger = logging.getLogger('PyEvolv')
    logger.setLevel(logging.DEBUG)
    
    log = logging.getLogger("giraffez.console_logger")
    log.setLevel(logging.INFO)
    
    if logger != None:
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)   
    # File handler
    fhandler = logging.FileHandler(file,'w', encoding='utf-8')
    fhandler.setLevel(logging.DEBUG)
    # Stream handler
    #shandler = logging.StreamHandler()
    #shandler.setLevel(logging.INFO)
    # formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    #shandler.setFormatter(formatter)
    # add handler to the logger
    logger.addHandler(fhandler)
    log.addHandler(fhandler)
    #logger.addHandler(shandler)
    
    return logger
