import os
import base64
#print(os.name) >> posix : linux | nt: Window

#os.system('touch f1 f2 f3 f4 f5 f6.dat')
print(os.getcwd())
originPath=os.getcwd()
os.chdir(originPath)
#os.system('touch f1 f2 f3 f4 f5 f6.dat')
os.chdir(originPath)
listA = os.listdir(originPath)

print(listA)

os.chdir(originPath)
def bdc(path):
    result = ""
    print("----------------------------------------------------------------------------------------------")
    print(">>>>>>>"+path)
    with open(path, 'w') as f:
        
        lines = f.readlines()
        for line in lines:
            line = line.encode('utf-8')
            result +=str(base64.encodestring(line))
        #f.write(result)
        print(result)
        print(path)
    
        # f.write(result)    

def f_all(i=0,fl=os.getcwd()):
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            path = os.path.join(root,name)
            print("="+path)
            npath ="."+('').join(path.split('.')[:2])
            print(npath)
            os.rename(path,npath +".txt")
            bdc(npath+".txt")
        for name in dirs:
            print(os.path.join(root, name))
            #   idx = filename.split('.')[0]
    #  i+=1


f_all()
