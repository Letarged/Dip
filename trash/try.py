#!/usr/bin/env python3

import threading
import time

def long_running_function():
    # simulate long running task
    time.sleep(5)


def display_loading():
    counter = 0
    while True:
        if counter % 6 == 0:
            print("\rLoading ", end="")
        print(".", end="", flush=True)
        time.sleep(0.5)
        counter += 1
        if counter >= 30:
            break

if __name__ == "__main__":
    loading_thread = threading.Thread(target=display_loading)
    loading_thread.start()

    long_running_function()

    loading_thread.join()