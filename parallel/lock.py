import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    # 공유변수(vavlue)
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, n):

        # Case 1
        # self._lock.acquire()
        # logging.info("Thread %s: acquire lock", n)
        # logging.info("Thread %s: starting update", n)
        #
        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy
        #
        # logging.info("Thread %s: ending update", n)
        # logging.info("Thread %s: release lock", n)
        # self._lock.release()

        # Case 2
        with self._lock:
            logging.info("Thread %s: acquire lock", n)
            logging.info("Thread %s: starting update", n)

            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info("Thread %s: ending update", n)
            logging.info("Thread %s: release lock", n)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )
    logging.info("Main Thread: before creating thread")

    store = FakeDataStore()

    logging.info('Testing update. Starting value is %d', store.value)

    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['Fisrt', 'Second', 'Third'] :
            executor.submit(store.update, n)

    logging.info('Testing update. Ending value is %d', store.value)
