import logging

class Log_Maker:
    @staticmethod
    def log_gen():    # Whenever the static method is created then, it will called by itself
        logging.basicConfig(filename=".\\logs\\nopcommerce.log",format='%(asctime)s:%(levelname)s:%(message)s',
                                            datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger()   # Creating one object
        logger.setLevel(logging.INFO)
        return logger

