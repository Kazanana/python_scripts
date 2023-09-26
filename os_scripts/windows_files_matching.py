import os
import fnmatch

path = '/mnt/c/Program Files'
dirs_MS = fnmatch.filter(os.listdir(path), '*Windows*')
dirs_Win = fnmatch.filter(os.listdir(path), '*Microsoft*')

joined_paths_MS = [os.path.join(path,file) for file in dirs_MS]
joined_paths_Win = [os.path.join(path,file) for file in dirs_Win]



print(fnmatch.filter(os.listdir('/mnt/c/Users/HP/python_scripts'), '*test*'))
test =[]
for name in  fnmatch.filter(os.listdir('/mnt/c/Users/HP/python_scripts'), '*test*'):
    if os.path.isdir(name):
        test.append(name)

print(test)