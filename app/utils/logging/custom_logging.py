import logging

logger = logging.getLogger("logging")

#### handler ####
fileHandler = logging.FileHandler("my_log.log")
consoleHandler = logging.StreamHandler()

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        fileHandler,
        consoleHandler
    ]
)
