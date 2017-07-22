# Display [projecteuler.net](https://projecteuler.net/) problems in terminal.
Developed in **Python 3.6.1**.

### Installing dependencies
Install pip, if you havent already, then run this command in terminal:
```
sudo pip install **beautifulsoup4 lxml**
```

### Usage
run the main, with wanted problem number:
```
# Prints the problem 'num' in the terminal emulator.
./main.py num 
```

### Recomendations
make an alias that executes the main
```
alias gler="~/gler/main.py"
```
so you can get the problem by just typing
```
geteuler num 
```
if you want to keep the alias after you close the terminal, add the alias to the terminal configuration file, mine was
```
~/.extend.bashrc 
```
