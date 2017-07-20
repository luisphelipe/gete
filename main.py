#!/usr/bin/python3

import bs4 as bs
import urllib.request
import sys

def main():

    exercise = sys.argv[1]
    
    # Try to convert parameter into integer.
    try:
        # Check if number is positive.
        if(int(exercise) < 1):
            print("The parameter must be positive")
            return     

    # Exception handling for when parameter isn't a number.
    except:
        print("The parameter must be a number")
        return
    
    # Try to get problem text from projecteuler.
    try:
        source = urllib.request.urlopen('https://projecteuler.net/problem='+ exercise)
        site = bs.BeautifulSoup(source,'lxml')

        problemName = site.find('h2')
        problemContent = site.find('div', {'class': 'problem_content'})
        print("\n", problemName.get_text(), "\n \n" ,problemContent.get_text(), "\n")
    
    # Exception handling for when there isn't a problem with such parameter(parameter too high), or when and random error occur.
    except:
        print("And error ocurred, maybe there is no exercise #{}".format(exercise))

if __name__ == "__main__": main()

