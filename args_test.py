import sys
import shutil
import os
import fnmatch

own_path = sys.argv[0]
#print(os.getcwd())
new_file = own_path[:own_path.find('.')] + "_dupa" + own_path[own_path.find('.'):]
#print(own_path)
# if os.path.exists(new_file):
#     new_file = new_file[:new_file.find('.')] + "_dupa" + new_file[new_file.find('.'):]
#     shutil.copyfile(own_path, new_file)

def new_file_name(path):
    new_path = path[:path.find('.')] + "_dupa" + path[path.find('.'):]
    if os.path.exists(new_path):
        return new_file_name(new_path)
    else:
        return new_path
    
#print(test(own_path))

shutil.copyfile(own_path, new_file_name(own_path))
