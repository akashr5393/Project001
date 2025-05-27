

import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger("automationLogger")  # Give it a specific name

        if not logger.handlers:  # Avoid adding multiple handlers
            log_dir = ".\\Logs"
            os.makedirs(log_dir, exist_ok=True)  # Ensure Logs directory exists

            fhandler = logging.FileHandler(filename=os.path.join(log_dir, 'automation.log'), mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)

            logger.setLevel(logging.INFO)

        return logger
