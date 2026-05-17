import argparse
import json
from src.core import NativeFeel

def main():
    parser = argparse.ArgumentParser(description='NativeFeel Agent Skill')
    parser.add_argument('--design', help='Design the cross-platform desktop app')
    parser.add_argument('--compile', help='Compile the designed app')
    args = parser.parse_args()
    if args.design:
        # Design the app
        pass
    elif args.compile:
        # Compile the app
        pass
if __name__ == '__main__':
    main()