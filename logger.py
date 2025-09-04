import logging

logging.basicConfig(level=logging.INFO, format="[CIA] %(message)s")

def log(msg): logging.info(msg)
