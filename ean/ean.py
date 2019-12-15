import argparse
import subprocess

def search(pkg, only_installed = False):
    flag = "-q --installed"
    if (not only_installed):
        flag = "-qaP"
        pkg = "'.*" + pkg + ".*'"

    cmd = ' '.join([ "nix-env", flag, pkg ])
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
    output = process.communicate()
    return (output[1] + ("\n" if output[1] else '') + output[0].rstrip("\n"))

def main():
    parser = argparse.ArgumentParser(prog="ean", description="An awesome Nix/NixOS cli wrapper")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    subparsers = parser.add_subparsers(title="Sub-command", dest="subcommand", help="")

    subSearch = subparsers.add_parser("search", help="Search available packages")
    subSearch.add_argument("-i", "--installed", action="store_true")
    subSearch.add_argument("pattern", help="Keyword or pattern of package name")

    subInstall = subparsers.add_parser("install", help="Install a package or more")
    subInstall.add_argument("package", help="Package name")

    subRemove = subparsers.add_parser("remove", help="Remove a package or more")
    subRemove.add_argument("package", help="Package name")

    subUpdate = subparsers.add_parser("update", help="Update selected or all channel")
    subUpdate.add_argument("channel", help="Package name")

    args = parser.parse_args()
    if args.subcommand == 'search':
        output = search(args.pattern)
    elif args.subcommand == 'install':
        output = install(args.package)
    elif args.subcommand == 'remove':
        output = remove(args.package)
    elif args.subcommand == 'update':
        output = update(args.channel)
    else
        parser.print_help()
        exit(0)

    print(output)
