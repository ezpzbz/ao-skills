import argparse

from tasklist import store


def main(argv=None):
    parser = argparse.ArgumentParser(prog="tasklist")
    sub = parser.add_subparsers(dest="cmd", required=True)
    add_p = sub.add_parser("add")
    add_p.add_argument("title")
    sub.add_parser("list")
    args = parser.parse_args(argv)

    if args.cmd == "add":
        task = store.add(args.title)
        print(f"added {task['id']}: {task['title']}")
    elif args.cmd == "list":
        for t in store.load():
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {t['id']}. {t['title']}")


if __name__ == "__main__":
    main()
