#!/usr/bin/python

from glob import glob
from HTMLParser import HTMLParser

class ArcherParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self) # old style class
        self._in_div = 0
        self._in_quote = False
        self._in_p = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if self._in_div or ('id', 'infinite') in attrs:
                self._in_div += 1
        elif tag == 'blockquote':
            if self._in_div:
                self._in_quote = True
        elif tag == 'p':
            if self._in_quote:
                self._in_p = True

    def handle_endtag(self, tag):
        if tag == 'div':
            if self._in_div:
                self._in_div -= 1
        elif tag == 'blockquote':
            if self._in_div:
                self._in_quote = False
                print '%'
        elif tag == 'p':
            if self._in_quote:
                self._in_p = False

    def handle_data(self, data):
        if self._in_p:
            print data.strip()

if __name__ == '__main__':
    parser = ArcherParser()

    for f in glob('pages/*'):
        for line in open(f):
            parser.feed(line)

