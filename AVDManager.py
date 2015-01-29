__author__ = 'liashi'

import argparse

def get_args():
    pass

def write_emu_binary():
    pass

def overwrite_build_prop():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AVD Manager")
    parser.add_argument("-c", "--create", help="Create specific AVD.")

    args = parser.parse_args()

    if args.create:
        pass