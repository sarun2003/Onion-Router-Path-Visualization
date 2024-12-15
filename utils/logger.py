import logging

# Configure logging
logging.basicConfig(
    filename="onion_router.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def log_message(message):
    logging.info(message)

def log_error(error):
    logging.error(error)
