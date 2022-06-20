#!/usr/bin/python3

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help="File to be split", type=str, required=True)
parser.add_argument("--lines", "-l", help="Maximum lines per split file", type=int, required=True)

args = parser.parse_args()
lines = args.lines
path = args.file


def split_data(data, chunks):
    result = []
    for item in data:
        result.append(item)
        if len(result) == chunks:
            yield result
            result = []
    yield result


with open(path) as input_file:
    index = 0
    for chunk in split_data(json.load(input_file), lines):
        with open(f"{path}_{index}", 'w') as chunk_file:
            index = index + 1
            chunk_file.write(json.dumps(chunk))

