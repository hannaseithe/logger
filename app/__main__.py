import time
from . import custom_logging as logging

def start_logging():
    while True:
        time.sleep(1)
        logging.log(message="Something happened")
        time.sleep(1)
        logging.log(message="Wrong level",level="banana")


def run():
    start_logging()

def main():
    print("App started")
    run()

main()