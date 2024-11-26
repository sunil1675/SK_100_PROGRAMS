import os
os.chdir("all prog\\")
dnm=os.listdir()

for i in range(len(dnm)):
    fnm=dnm[i]
    print(f"Opening {fnm} File for processing........ ")
    f=open(fnm,encoding='utf-8')
    s=f.read()
    s=s.replace("SRISHTI","SUNIL SIR")
    s=s.replace("srishti","SUNIL SIR")
    s=s.replace("Srishti","SUNIL SIR")
    f.close()
    
    f=open(fnm,'w',encoding='utf-8')
    f.write(s)
    f.close()
    
        
    





    
