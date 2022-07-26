import logging
import pathlib
from datetime import datetime



logging.root.level = logging.DEBUG

root = pathlib.Path(__file__).parent
logs_path = root.joinpath("logs_practice")

try:
    logs_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)


log_file_name = datetime.now().strftime("%d%m%Y_%H%M%S.log")
log_abs_path = logs_path.joinpath(log_file_name)


logging.basicConfig(filename=log_abs_path, encoding='utf-8', level=logging.DEBUG, filemode="w")
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


print(f"File name{__file__}")


print(root)