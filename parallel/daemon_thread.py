import logging
import threading
import time

def thread_func(name, rng):
    logging.info("Sub Thread %s: starts", name)
    for i in rng:
        print(i)
    logging.info("Sub Thread %s: end", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )
    logging.info("Main Thread: before creating thread")

    # Finish when main thread complete
    x = threading.Thread(target=thread_func, args=("First",range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=("Second",range(10000)), daemon=True)

    x.start()
    y.start()

    print(x.isDaemon())

    # daemon become no effect when use join
    # x.join()
    # y.join()

    logging.info("Main Thread: wait for the thread to finish")

    logging.info("Main Thread: all done")
