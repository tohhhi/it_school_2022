import logging
import pathlib
from datetime import datetime


LOGGER_NAME = "main_logger"

# Formatul
message_only = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")


verbose = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(filename)s - %(lineno)d - %(message)s')



# handler configurat pentru consola:


handler_for_console = logging.StreamHandler()

handler_for_console.formatter = message_only

logger = logging.getLogger(LOGGER_NAME)


logger.addHandler(handler_for_console)

logger.setLevel(logging.DEBUG)



# handler configurat sa salveze mesaje in fisier;

root = pathlib.Path(__file__).parent

logs_path = root.joinpath("logs_practice_3")

try:
    logs_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)


log_file_name = datetime.now().strftime("%d%m%Y_%H%M%S.log")
log_abs_path = logs_path.joinpath(log_file_name)

handler_for_file = logging.FileHandler(log_abs_path)
handler_for_file.setLevel(logging.ERROR)
handler_for_file.formatter = verbose

logger.addHandler(handler_for_file)


# MAIN 


user_name = "Ionut"

logger.info("Starting....")
logger.debug(f"Execution started at {datetime.now()}")

logger.info("Creating database...")
logger.info("Database created.")


logger.info(f"Creating invoice for {user_name}...")
# fct pentru facturi
logger.error("Could not create invoice!")

logger.info("Generating report...")
# fct pt raport
logger.info("Report done.")

logger.debug("Closing database connection....")
logger.error("Database is corrupt...aborting.")
logger.critical("System crash, due to no database instance.")