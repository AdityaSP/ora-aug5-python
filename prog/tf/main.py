import sys
import unittest
if len(sys.argv) == 2:
    fp=sys.argv[1]
else:
    print("Provide a test pack config csv")
    exit(1)

fh = open(fp, 'rt')
    
ts = unittest.TestSuite()
for idx,line in enumerate(fh):
    if idx ==0 or line.startswith('#'):
        continue
    cols = line.split(",")
    if cols[-1].strip() == 'n':
        continue
    #1. 'import ' 'cols[0]'
    exec('import ' + cols[0])
    #2. add the testcase
    ts.addTest(eval( "{}.{}('{}')".format(cols[0],cols[1],cols[2])))
    #print("{}.{}('{}')".format(cols[0],cols[1],cols[2]))
    
r = unittest.TextTestRunner(verbosity=3)
r.run(ts)
    
fh.close()