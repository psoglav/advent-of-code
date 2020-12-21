with open('input.txt', 'r') as f:
  nums = [int(num) for num in f.readlines()]
  
  for i in nums:
    for k in nums:
      for j in nums:
        if i + k + j == 2020:
          print(f'{i} * {k} * {j} = {i * k * j}')