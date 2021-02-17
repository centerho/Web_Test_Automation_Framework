import logging
from datetime import datetime

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename='.\\logs\\Auto.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        filename = datetime.now().strftime(".\\logs\\automation_%Y%m%d%H%M%S.log")
        fileHandler = logging.FileHandler(filename, encoding="utf-8")
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)
        return logger