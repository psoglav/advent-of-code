import re

with open('input.txt', 'r') as f:
  lines = f.readlines()
  valid = 0
  
  for line in lines:
    _range, _letter, _pass = line.strip().split(' ')
    
    _range = _range.split('-')
    _range = int(_range[0]), int(_range[1])
    
    _letter = _letter[0]
    
    left =  _pass[_range[0] - 1] == _letter 
    right =  _pass[_range[1] - 1] == _letter
    
    if (left and not right) or (right and not left):
      valid += 1
      
  print(valid)
  