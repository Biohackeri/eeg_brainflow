
import glob
files = glob.glob("Recordings\*")

for file_name in files:
    out_file_name = "Filter\\"+file_name.split('\\')[1]
    
    f = open(out_file_name+'.fil', "w")

    with open(file_name) as file:
        #remove OPENBCI GUI header
        for _ in range(5):
            file.readline()
        
        # format to tabbed space
        # removed formatted timestamp at the end
        # add new line
        for line in file:
            out = '\t'.join(line.split(',')[:-1])+'\n'
            f.write(out)

    f.close()
    

