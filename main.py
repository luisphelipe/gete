#!/usr/bin/python3

import bs4 as bs
import urllib.request
import sys

def main():

    exercise = sys.argv[1]

    source = urllib.request.urlopen('https://projecteuler.net/problem='+ exercise)
    site = bs.BeautifulSoup(source,'lxml')

#    problemName = site.find('div', {'id': 'problem_info'})
    problemContent = site.find('div', {'class': 'problem_conten'})
    print(problemContent.get_text())

if __name__ == "__main__": main()

