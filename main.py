#!/usr/bin/python3


import csv
import argparse


def parse_arguments(parser):
    parser.add_argument('-f', '--file', help='Lastpass csv file')
    parser.add_argument('-v', '--verbose', help='Print logs on screen', action='store_true')
    args = parser.parse_args()
    return args.file, args.verbose


def log(msg):
    global verbose
    if verbose:
        print(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    file, verbose = parse_arguments(parser)
    if not file:
        parser.exit(1, parser.print_help())

    with open(file, mode='r') as csv_in, open('bitwarden_output.csv', 'w', newline='') as csv_out:
        csv_reader = csv.DictReader(csv_in)
        csv_writer = csv.DictWriter(csv_out, fieldnames=['url', 'username', 'password', 'totp', 'extra', 'name', 'grouping', 'fav'])
        csv_writer.writeheader()
        line_count = 0
        modified_row = {}
        for row in csv_reader:
            if len(row['password']) > 512:
                modified_row = {**row, 'password': 'Unavailable. Go to your Lastpass vault to find that info'}
                csv_writer.writerow(modified_row)
                continue
            if len(row['extra']) > 512:
                modified_row = {**row, 'extra': 'Unavailable. Go to your Lastpass vault to find that info'}
                csv_writer.writerow(modified_row)
                continue
            csv_writer.writerow(row)
            line_count += 1
        print(f'Processed {line_count} lines.')
