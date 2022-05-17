
import glob
files = glob.glob("Recordings\*")

for file_name in files:
    f = open(file_name+'.fil', "w")

    with open(file_name) as file:
        for _ in range(5):
            file.readline()
        
        for line in file:
            #print(line.split())
            #print(len(line.split()))
            out = '\t'.join(line.split(',')[:-1])+'\n'
            #print(out.split())
            #print(len(out.split()))
            f.write(out)

            
    f.close()

