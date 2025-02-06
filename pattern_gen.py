#!/usr/bin/python3

import sys, argparse, re

green = "\033[1;32;40m"
end = "\033[0m"
darkGray = "\033[1;30m"
red = "\033[0;31m"
lightPurple = "\033[1;35m"

parser = argparse.ArgumentParser(
        description = "%spatern generator for buffer overflow%s" % (lightPurple, end),
        usage = "pattern.py -m [generate|offset] -v [lines|eip value]"
        )

parser.add_argument("-m", "--mode", required=True, type=str, help="mode")
parser.add_argument("-v", "--value", required=True, help="lines to generate or the value to calculate offset")

args = parser.parse_args()

mode = args.mode
value = args.value

def generate(lines):

    if lines >= 6319:
        print("\n%s[!]%s too much data\n" % (red, end))
        sys.exit(1)

    chars = "abcdefghijklmnopqrstuvwxyz"

    count = 0

    result = ""

    for c in chars:
        for i in range(0,9):
            for i2 in range(0,9):
                result += "%s" % (c)
                count += 1
                if count == lines:
                    return result
                result += "%s" % (i)
                count += 1
                if count == lines:
                    return result
                result += "%s" % (i2)
                count +=1
                if count == lines:
                    return result

def getOffset(match):

    found = 0

    for m in re.compile("%s" % match).finditer(generate(6318)):
        print("\n%s[*]%s offset %s%s%s" % (green, end, green, m.start(), end))
        found = 1
    
    if found == 0:
        print("\n%s[!]%s couldnt found that match\n" % (red, end))

def main():

    if args.mode == "generate":
    
        print("\n%s[*]%s generating %s%s%s bytes of pattern...\n\n" % (green, end, green, int(value), end))

        print(generate(int(value)))


    if args.mode == "offset":
    
        getOffset(value)


if __name__ == '__main__':

    main()
