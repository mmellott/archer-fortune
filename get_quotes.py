#!/usr/bin/python

from subprocess import call

# quote source
WEBSITE = 'http://www.tvfanatic.com/quotes/shows/archer/'

# for now, just check website for this value
NUM_PAGES = 55

call(['mkdir', '-p', 'pages'])
for i in range(1, NUM_PAGES+1):
    page = ''
    if i != 0:
        page = 'page-{}.html'.format(i)

    call(['wget', '-O', 'pages/{:02}'.format(i), WEBSITE + page])

