#this program lists all the contenets of a given directory and renames the files
#that begin with a number so as to reveal the encoded secret message
import os

def rename_files(dir_in, rm_in):
    #get file names from the directory
    file_list = os.listdir(uinput)
    #print file_list
    #get initial directory
    saved_path = os.getcwd()
    #change to directory with relevant files to rename
    os.chdir(uinput)

    #rename files to names without numbers
    for file_name in file_list:
        print "Old name: "+file_name
        os.rename(file_name, file_name.translate(None, rm_in))
        print "New name: "+file_name.translate(None, rm_in)
        print ""
    #change back to initial directory
    os.chdir(saved_path)

dir_in = raw_input("Enter/copy the dirctory path with files you want to rename : ")
rm_in = raw_input("What would you like to remove from the file(s) ? : ")
rename_files(dir_in, rm_in)
