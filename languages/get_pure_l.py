import csv

fname = 'languages.yml'
how_many = 0

with open('all-languages.csv', 'wb') as csvfile:
    outputter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    with open(fname) as f:
        content = f.readlines()
        for c in content:
            if (c.strip().endswith(':') == True) and (c.count('aliases') < 1) and (c.count('extensions') < 1) and (c.count('filenames') < 1):
                outputter.writerow([str(c.strip().replace(':',''))])
                how_many = how_many + 1
print how_many
csvfile.close()