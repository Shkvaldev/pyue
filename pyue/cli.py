import os
import sys
import shutil
import argparse
from loguru import logger

from .__version__ import __version__
from .__root__ import __root__


def main():
    parser = argparse.ArgumentParser(description="Pyue management tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    init_parser = subparsers.add_parser(
        "init", aliases=["i"], help="Initialize a new project"
    )
    init_parser.add_argument(
        "project_name",
        nargs="?",
        default="./",
        help="Project name or directory (default: current directory)",
    )

    build_parser = subparsers.add_parser(
        "build", aliases=["b"], help="Build the project"
    )
    build_parser.add_argument(
        "--destination", "-d", dest="target", help="Specific destination to build"
    )

    subparsers.add_parser("version", aliases=["v"], help="Get project version")

    args = parser.parse_args()

    if args.command in ["init", "i"]:
        handle_init(args)
    elif args.command in ["build", "b"]:
        handle_build(args)
    elif args.command in ["version", "v"]:
        print(f"Current version is `{__version__}`")
    else:
        parser.print_help()
        sys.exit(1)


def handle_init(args):
    project_path = args.project_name
    try:
        skel_path = os.path.join(__root__, "skel")

        if project_path in ["./", "."]:
            target_dir = os.path.join(os.getcwd(), os.path.basename(os.getcwd()))
            logger.info(
                f"No project name specified, using current directory name: {os.path.basename(os.getcwd())}"
            )
        else:
            target_dir = os.path.join(os.getcwd(), project_path)

        logger.debug(f"Target directory: {target_dir}")

        os.makedirs(target_dir, exist_ok=False)

        for item in os.listdir(skel_path):
            if item == "__pycache__":
                continue

            src = os.path.join(skel_path, item)
            dst = os.path.join(target_dir, item)

            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        logger.success(f"Project initialized in {target_dir}")

    except Exception as e:
        logger.error(f"Failed to init project: {e}")
        exit(-1)


def handle_build(args):
    logger.debug("Building project...")
    target = "./"
    if args.target:
        target = args.target
    print(f"  Target: {target}")


if __name__ == "__main__":
    main()
