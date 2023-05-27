import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]    ###toreplace root name with class name
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\Automation selinium\\Automation testing python selinium tushar sir\\OrangeHRM Project\\Logs\\OrangeHrm_Automation.Logs")
        Format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")
        logfile.setFormatter(Format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
