import os
import csv
import datetime
import fnmatch

# #odczytywanie z csv do listy
# plik_z_zestawieniem = '/mnt/c/Users/HP/python_scripts/zestawienie_exe.csv'

# with open(plik_z_zestawieniem, 'r') as f:
#     reader_obj = csv.reader(f)
#     lista_z_pliku = []
#     for row in reader_obj:
#         lista_z_pliku.append(row)

# # print(lista_z_pliku)


folder_path = '/mnt/c/Program Files'
exe_files = []
sciezka_zestawienia = '/mnt/c/Users/HP/python_scripts/zestawienie_exe_Program_Files.csv'


for root, dirnames, filenames in os.walk(folder_path):
    for file in fnmatch.filter(filenames, '*.exe'):
        #Unix timestamp
        mod_time = os.path.getmtime(os.path.join(root,file))
        exe_files.append([os.path.join(root,file),mod_time])


for i, time_element in enumerate(exe_files):
    new_time_format = datetime.datetime.fromtimestamp(time_element[1])
    new_time_format = new_time_format.strftime("%d-%m-%GT%H%M%S")
    exe_files[i][1] = new_time_format

with open(sciezka_zestawienia, 'w') as f:
    f.write('Pełna ścieżka do pliku, data ostatniej modyfikacji\n')

with open(sciezka_zestawienia, 'a') as f:
    for element in exe_files:
        f.write(f'{element[0]},{element[1]}\n')
    



