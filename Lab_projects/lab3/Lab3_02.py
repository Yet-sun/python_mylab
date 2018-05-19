import sys

f_handler = open('out.txt', 'w')
sys.stdout = f_handler
print('hello')