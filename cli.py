import argparse

from pe_patcher import enable_4GB
from gui import run_gui

def run_cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true")
    parser.add_argument("path", nargs='?')

    args = parser.parse_args()

    if(args.gui):
        run_gui()
    else:
        message = enable_4GB(args.path)
        print(message)

