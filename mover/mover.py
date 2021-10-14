#! /usr/local/bin/python3
import datetime as dt
import argparse
import time
import AppKit
from typing import Sequence
import pyautogui
from pyautogui import KEYBOARD_KEYS


DEFAULT_RUNTIME = 30 * 60  # 30 minutes


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-time-hours', '-rt', nargs=1, help='total hours for the script to run before exiting')
    res = parser.parse_args(argv)

    run_mover(float(res.run_time_hours[0]) * 60 * 60 if res.run_time_hours else DEFAULT_RUNTIME)

    return 0


def run_mover(TOTAL_RUNTIME: int) -> None:
    formatted = dt.timedelta(seconds=TOTAL_RUNTIME)
    print(f"running for {str(formatted)} hours!")

    start_time = time.time()
    end_time = start_time + TOTAL_RUNTIME

    while time.time() < end_time:
        print("pressing!")
        pyautogui.press("capslock")
        pyautogui.press("capslock")
        time.sleep(30)


if __name__ == "__main__":
    raise SystemExit(main(["--run-time-hours", "0.5"]))
