import os
import logging
from datetime import datetime
import sqlite3

def init_logging(log_level='DEBUG'):
    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')

    logger = logging.getLogger(__name__)
    logger.setLevel(numeric_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')

    log_dir = 'log'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f'log_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log')
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

def init_db(data_conn='./data/database.db'):
    db_dir = os.path.dirname(data_conn)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    conn = sqlite3.connect(data_conn)
    return conn