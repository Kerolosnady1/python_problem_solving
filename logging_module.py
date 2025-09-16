import logging

# print(dir(logging))

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("Elzero")

my_logger.warning("This Is Warning Message")