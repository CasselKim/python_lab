import logging
import threading
import time

def thread_func(name):
    logging.info("Sub Thread %s: starts", name)
    time.sleep(3)
    logging.info("Sub Thread %s: end", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )
    logging.info("Main Thread: before creating thread")

    x = threading.Thread(target=thread_func, args=("First",))

    x.start()

    # Wait for Sub thread
    # x.join()

    logging.info("Main Thread: wait for the thread to finish")

    logging.info("Main Thread: all done")
