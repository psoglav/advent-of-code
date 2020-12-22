import re


with open('input.txt', 'r') as f:
  docs = f.read().split('\n\n')
  docs = [re.split(r'[\n\s]', doc) for doc in docs]
  required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
  ]
  
  for fields in docs:
    for i, field in enumerate(fields):
      key, value = field.split(':')
      fields[i] = {
        key: value
      }
      
  valid = [1 for _ in range(len(docs))]
      
  for docid, doc in enumerate(docs):
    for require in required:
      # part one
      keys = [list(field.keys())[0] for field in doc]
      
      if not require in keys:
        valid[docid] = 0
        break
    
    if not valid[docid]:
      continue
        
    # part two
    document = doc[0].copy()
    
    for field in doc:
      document |= field
      
    fbyr = document['byr']
    fiyr = document['iyr']
    feyr = document['eyr']
    fhgt = document['hgt']
    fhcl = document['hcl']
    fecl = document['ecl']
    fpid = document['pid']
    
    byr = re.match(r'^\d{4}$', fbyr) and 2002 >= int(fbyr) >= 1920
    iyr = re.match(r'^\d{4}$', fiyr) and 2020 >= int(fiyr) >= 2010
    eyr = re.match(r'^\d{4}$', feyr) and 2030 >= int(feyr) >= 2020
    hgt = re.match(r'^(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)$', fhgt)
    hcl = re.match(r'^#[0-9a-f]{6}$', fhcl)
    ecl = fecl in 'amb blu brn gry grn hzl oth'.split()
    pid = re.match(r'^[0-9]{9}$', fpid)
    
    if not (byr and iyr and eyr and hgt and hcl and ecl and pid):
      valid[docid] = 0


print('valid:', valid.count(1))