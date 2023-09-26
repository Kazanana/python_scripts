#ze ścieżki mnt/c Program files znaleźć wszytkie pliki exe
#sprawdzić ich daty ostatniego modyfikowania
# zapisać do listy jeśli ostatnia modyfikacja była dawniej niż 2 miesiące temu

import os
import fnmatch
import datetime

exe_files = []
sciezka_zestawienia = '/mnt/c/Users/HP/python_scripts/zestawienie_exe.csv'


for root, dirnames, filenames in os.walk('/mnt/c/Program Files/Autodesk'):
    for file in fnmatch.filter(filenames, '*.exe'):
        #Unix timestamp
        mod_time = os.path.getmtime(os.path.join(root,file))
        exe_files.append([os.path.join(root,file),mod_time])


for i, time_element in enumerate(exe_files):
    new_time_format = datetime.datetime.fromtimestamp(time_element[1])
    new_time_format = new_time_format.strftime("%d-%m-%GT%H%M%S")
    exe_files[i][1] = new_time_format
    


# print(exe_files)
with open(sciezka_zestawienia, 'w') as f:
    f.write('Pełna ścieżka do pliku, data ostatniej modyfikacji\n')

with open(sciezka_zestawienia, 'a') as f:
    for element in exe_files:
        f.write(f'{element[0]},{element[1]}\n')

# two_months_ago = datetime.datetime.now() - datetime.timedelta(days = 60)

# count = 0
# for i in exe_files:
#     if datetime.datetime.fromtimestamp(i[1]) < two_months_ago:
#         #print(i)  
#         count += 1
# print(count)
