import logging
import pathlib
from datetime import datetime

logging.root.level = logging.DEBUG
root = pathlib.Path(__file__).parent
logs_path = root.joinpath("area.logs")

try:
    logs_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)

log_file_name = datetime.now().strftime("%d%m%Y_%H%M%S.log")
logs_abs_path = logs_path.joinpath(log_file_name)

logging.basicConfig(filename=logs_abs_path, level=logging.DEBUG, filemode="w")

logging.info("We will calculate area of a circle.")

def area_circle(r):
    
    return r * 3.14 ** 2


logging.debug("Aria of the circle is:")

print = logging.debug
print(area_circle(4))


logging.info("We will calculate area of a rectangle.")

def area_of_rectangle(L,l):
    return L * l


logging.debug(f"The area of a rectangle is:")
print = logging.debug
print(area_of_rectangle(20,5))




