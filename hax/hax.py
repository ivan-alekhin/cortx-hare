from hax.halink import HaLink
from hax.types import Fid
import logging
import threading


def setup_logging():
    logging.basicConfig(level=logging.DEBUG)


def thread_fn(ha: HaLink):
    ha.test()


def main():
    setup_logging()
    l = HaLink(node_uuid="This is a test")
    # l.start("endpoint", Fid(3,4), Fid(5,6), Fid(0xDEADBEEF, 7))
    logging.info("Invoking threads")

    threads = [None] * 20
    threads = list(map(lambda t: threading.Thread(target=thread_fn, args=(l,)), threads))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    logging.info("Threads finished")


if __name__ == "__main__":
    main()