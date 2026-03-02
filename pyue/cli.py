import argparse
import sys

from . import __version__

def main():
    parser = argparse.ArgumentParser(description='Pyue management tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    init_parser = subparsers.add_parser('init', aliases=['i'], help='Initialize a new project')
    init_parser.add_argument('project_name', nargs='?', default='.', help='Project name or directory (default: current directory)')
    
    build_parser = subparsers.add_parser('build', aliases=['b'], help='Build the project')
    build_parser.add_argument('--destination', '-d', dest='target', help='Specific destination to build')
    
    subparsers.add_parser('version', aliases=['v'], help='Get project version')

    args = parser.parse_args()
    
    if args.command in ['init', 'i']:
        handle_init(args)
    elif args.command in ['build', 'b']:
        handle_build(args)
    elif args.command in ['version', 'v']:
        print(f"Current version is `{__version__}`")
    else:
        parser.print_help()
        sys.exit(1)

def handle_init(args):
    project_path = args.project_name
    print(f"Initializing project in: ./{project_path}")

def handle_build(args):
    print("Building project...")
    target = "./"
    if args.target:
        target = args.target
    print(f"  Target: {target}")

if __name__ == "__main__":
    main()
