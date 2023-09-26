#nauka_os_module

import os
import fnmatch

#znajdź wszystkie pliki pdf w folderze z książkami
#zapisz je do listy
#zapisz każdy element listy jako oddzielna linia do pliku tekstowego
matches_pdf = []
matches_mobi = []
matches_epub = []
matches_else = []
dirs = []
files_num = 0
for root, dirnames, filenames in os.walk('/mnt/c/Users/HP/books'):
    # dirs.append(os.path.join(root, dirnames[0][i]))
    if len(dirnames) != 0:
        for d in dirnames: 
            dirs.append(d)
    files_num += len(filenames)
    for filename in filenames:
        if fnmatch.fnmatch(filename, '*.pdf'):
            matches_pdf.append(os.path.join(root, filename))
        elif fnmatch.fnmatch(filename, '*.epub'):
            matches_epub.append(os.path.join(root, filename))
        elif fnmatch.fnmatch(filename, '*.mobi'):
            matches_mobi.append(os.path.join(root, filename))
        else:
            matches_else.append(os.path.join(root, filename))
        # matches.append(os.path.join(root, filename))

# print(matches_pdf)
# print(matches_epub)
# print(matches_mobi)
# print(matches_else)
# print(dirs)

with open('books_metadata.txt', 'w') as f:
    f.write('Informacje na temat folderu /mnt/c/Users/HP/books\n')

with open('books_metadata.txt', 'a') as f:
    f.write(f'Ilość wszystkich plików: {files_num}\n')
    f.write('Lista katalogów:\n')
    for match in dirs:
        f.write(f'{match}\n')
    f.write('Lista plików pdf:\n')
    for match in matches_pdf:
        f.write(f'{match}\n')
    f.write('Lista plików epub:\n')
    for match in matches_epub:
        f.write(f'{match}\n')
    f.write('Lista plików mobi:\n')
    for match in matches_mobi:
        f.write(f'{match}\n')
    f.write('Lista plików w innych formatach:\n')
    for match in matches_else:
        f.write(f'{match}\n')

print(len(matches_pdf) + len(matches_epub) + len(matches_mobi) + len(matches_else))







