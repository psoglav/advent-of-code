with open('input.txt', 'r') as f:
  airplane = [[(c, r) for c in range(8)] for r in range(128)]
  passes = f.readlines()
  ids = []
  
  for p in passes:
    curr = airplane.copy()
    directions = list(p.strip())
    
    # looking for row:
    # F - lower half
    # B - upper half
    for i in range(7):
      half = len(curr) // 2
      length = len(curr)
      
      if directions[i] == 'F': 
        curr = curr[:half]
      elif directions[i] == 'B': 
        curr = curr[half:length]
    
    row = curr[0]
    
    # looking for column (row + column = seat)
    # L - lower half
    # R - upper half
    for i in range(6, 10):
      half = len(row) // 2
      length = len(row)
      
      if directions[i] == 'L': 
        row = row[:half]
      elif directions[i] == 'R': 
        row = row[half:length]
        
    col, row = row[0]
    id = row * 8 + col
    ids.append(id)
      
    # print(p)
    # print('row:', row, 'col:', col)
    # print('ID:', id)
    # print()
    
  # answer of part one
  print('highest ID:', max(ids))
    
  # answer of part two
  for i in range(7, 909):
    if not i in ids: print('my seat id:', i)
  