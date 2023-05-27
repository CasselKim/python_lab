import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info("Sub Thread %s: starting", name)

    result=0
    for i in range(10001):
        result = result+i

    logging.info("Sub Thread %s: finish result : %d", name, result)
    return result


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt="%H:%M:%S",
    )
    logging.info("Main Thread: before creating thread")

    # Case 1
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task, ("First",))
    task2 = executor.submit(task, ("Second",))

    print(task1.result())
    print(task2.result())

    # Case 2
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ["First", "Second"])

        print(list(tasks))


if __name__ == "__main__":
    main()