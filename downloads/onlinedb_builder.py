import os

## this builds onlinedb.txt

cur = os.getcwd()
txt = cur + '\\' + 'onlinedb.txt'
dirs = os.listdir(cur)
onlinedb = []
i = 0
with open(txt, 'w') as out:

    for d in dirs:
        if '.' not in d and '_' not in d:
            fpath = cur + '\\' + d
            files = os.listdir(fpath)

            for f in files:
                f = f.replace('-', ' ')
                f = f[:-4]
                onlinedb.append(d + ' ' + f)
                out.write(onlinedb[i] + '\n')
                i+=1
