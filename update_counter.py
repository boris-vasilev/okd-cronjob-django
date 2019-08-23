#!/usr/bin/env python

if __name__ == "__main__":
    with open('counter', 'r') as f:
        counter = int(f.read())
    with open('counter', 'w+') as f:
        f.write(str(counter + 1))