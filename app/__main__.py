import time
from . import custom_logging as logging

def start_logging():
    while True:
        time.sleep(1)
        logging.log("Something happened")


def run():
    start_logging()

def main():
    print("App started")
    run()

main()