import argparse
import sys

import shodan

API_KEY = "cjJ9R7Hi0y4Vfj66wrkISnUyeGmqGeYn"


def myip_subcommand(args):
    api = shodan.Shodan(API_KEY)
    print("IP Address:", api.tools.myip())


def host_subcommand(args):
    api = shodan.Shodan(API_KEY)
    host = api.host(args.host)

    for key in host:
        if key == "data":
            continue

        data = ','.join(map(str, host[key])) if isinstance(host[key], list) else host[key]

        print("{}: {}".format(key, data))


def search_subcommand(args):
    api = shodan.Shodan(API_KEY)
    matches = api.search(args.query)['matches']

    for match in matches:
        ip = match['ip_str'].ljust(20)
        port = str(match['port']).ljust(10)
        org = (match['org'] if match['org'] else '').ljust(50)

        print(ip, port, org, ','.join(match['hostnames']))


def main(argv):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    myip_parser = subparsers.add_parser('myip')
    myip_parser.set_defaults(func=myip_subcommand)

    host_parser = subparsers.add_parser('host')
    host_parser.add_argument("host")
    host_parser.set_defaults(func=host_subcommand)

    search_parser = subparsers.add_parser('search')
    search_parser.add_argument("query")
    search_parser.set_defaults(func=search_subcommand)

    args = parser.parse_args(argv[1:])
    args.func(args)


if __name__ == "__main__":
    main(sys.argv)
