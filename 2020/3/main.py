total = 1

with open('input.txt', 'r') as f:
  _map = [row.strip() for row in f.readlines()]

def TOTW(right, down): # Trees On The Way
    trees, x, y = 0, 0, 0
    
    while y < len(_map) - 1:
      x += right
      y += down
      cell = _map[y][x % len(_map[y])]
      
      if cell == '#':
        trees += 1
      
    return trees

  
trees_total = []

answers = []

# answer for part 1
answers.append(TOTW(right=3, down=1))
# answer for part 2
slopes = [
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2),
]

for slope in slopes:
  total *= TOTW(*slope)

answers.append(total)


print(answers)