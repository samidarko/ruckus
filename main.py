#!/usr/bin/env python
import re

def clean_line(line):
    line = line.replace('.', '')
    line = line.replace(',', '')
    line = line.replace('"', '')
    line = line.strip()
    return line

def pretty_print(data):
    for key, value in sorted(data.items(), key=lambda item: item[1], reverse=True):
        print("%s: %s" % (key, value))

# TODO [True???] ?
# TODO all words should be lowercase

def main():

    data = {}

    with open('stoic_philosophy_of_mind') as f:

        for line in f.readlines():
            new_line = clean_line(line)
            if new_line:
                array_line = new_line.split(' ')
                for word in array_line:
                    if word in data:
                        data[word] += 1
                    else:
                        data[word] = 1

        return data

if __name__ == "__main__":
    pretty_print(main())
