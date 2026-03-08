import argparse
import sys
from pathlib import Path

# Ensure project root is on sys.path  
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from train import train_main
from predict import predict_main


def main(argv=None):
	parser = argparse.ArgumentParser(prog='main')
	sub = parser.add_subparsers(dest='cmd')
	sub.add_parser('train')
	sub.add_parser('predict')
	args, rest = parser.parse_known_args(argv)
	if args.cmd == 'train':
		train_main(rest)
	elif args.cmd == 'predict':
		predict_main(rest)
	else:
		parser.print_help()


if __name__ == '__main__':
	main(sys.argv[1:])