#różne rzeczy z modyfikacją pdfów

from pypdf import PdfReader, PdfWriter
import pdfkit
import platform

def modify_path_string(path):
    if platform.system() == "Windows":
        path = path.replace('/mnt/c', 'C:')
        path = path.replace('/', '\\')
        return path
    else:
        return path
    
def stalowy_pdf(path,out):
    pdfReader = PdfReader(path)
    pagesObj = pdfReader.pages[:]
    #pdfWriter = PdfWriter()
    pdfString = ''
    for page in pagesObj:
        pdfString += (page.extract_text())
        #pdfWriter.add_page(page)
        #print(page.extract_text())
    pdfkit.from_string(pdfString, out)

stalowy = '/mnt/c/Users/HP/Downloads/Skuteczne-Suplementy.-Decydujaca-Przewaga-STALOWY-SZOK.pdf'
stalowy_clean = stalowy.replace('.pdf', '_clean.pdf')



# w pętli utworzyć pusty plik pdf, utworzyć obiekt pdfWriter dla tego pliku i dodać do niego odpowiednie strony
def dokumenty_ING(folder):
    #folder = '/mnt/c/Users/HP/dokumenty/dokumenty_ING/'
    dokumenty = folder + 'Dokumenty+dot.+zatrudnienia_Umowa+o+Prace_edit.pdf'

    ankietaPersonalna = folder + 'Kazana_Dominik_AnkietaPersonalna.pdf'
    ZUS_US = folder + 'Kazana_Dominik_ZUS+US+Oświadczenie+do+celów+KUP.pdf'
    PIT_2 = folder + 'Kazana_Dominik_PIT-2.pdf'
    do26RokuZycia = folder + 'Kazana_Dominik_Oświadczenie+podatnika+do+ukończenia+26+roku+życia+o+przychodach+w+2023.pdf'

    pdf_reader = PdfReader(dokumenty)

    working_dir = {ankietaPersonalna: (12, 14), ZUS_US: (15), PIT_2: (16, 18), do26RokuZycia: (22) }
    for key in working_dir:
        pdf_writer = PdfWriter()  # we want to reset this when starting a new pdf
        #print(f"Key:{key}, dict[key]: {working_dir[key]}, type(dict[key]): {type(working_dir[key])}")
        if type(working_dir[key]) is int:
            pdf_writer.add_page(pdf_reader.pages[working_dir[key] - 1])
        else:
            for idx in range(working_dir[key][0] - 1, working_dir[key][1]):
                pdf_writer.add_page(pdf_reader.pages[idx])
        output_filename = key
        with open(output_filename, "wb") as out:
            pdf_writer.write(out)


#stalowy_pdf(stalowy, stalowy_clean)
folder = '/mnt/c/Users/HP/dokumenty/dokumenty_ING/'
dokumenty_ING(modify_path_string(folder))
#print(stalowy_clean)
            
             


