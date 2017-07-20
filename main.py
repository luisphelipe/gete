#!/usr/bin/python3

import bs4 as bs
import urllib.request
import sys

def main():

    exercise = sys.argv[1]
    
    if(exercise < 1 or not isinstance(exercise, int) ):
        print("The wanted exercise number must be a positive integer")
        return

    try:
        source = urllib.request.urlopen('https://projecteuler.net/problem='+ exercise)
        site = bs.BeautifulSoup(source,'lxml')

        problemName = site.find('div', {'id': 'problem_info'})
        problemContent = site.find('div', {'class': 'problem_content'})
        print("\n", problemName.get_text(), "\n \n" ,problemContent.get_text(), "\n")
    except:
        print("And error ocurred, maybe there is no exercise #{}".format(exercise)

if __name__ == "__main__": main()

