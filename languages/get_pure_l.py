fname = 'languages.yml'
how_many = 0

with open(fname) as f:
    content = f.readlines()
    for c in content:
        #print c
        if (c.strip().endswith(':') == True) and (c.count('aliases') < 1) and (c.count('extensions') < 1) and (c.count('filenames') < 1):
            print c
            how_many = how_many + 1;
print how_many