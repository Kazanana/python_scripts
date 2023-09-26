import ebooklib
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from ebooklib import epub

#chuyjowo tłumaczy ten translator


#mam wyekstrachowane czaptery
#wyciągnąć paragrafy z czaptera i załadować [x]
#zamienić na stringa i jeśli dłuższy niż 5k to podzielić[x]
#wysyłać do tłumaczenia i zapisywać przetłumaczone
#jakoś to złożyć do kupy :^)

book = epub.read_epub('/mnt/c/Users/HP/python_scripts/Alices_Adventures_in_Wonderland.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

chapters_list=[]
for item in items:
    chapters_list.append(item)


def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)
def divide_chapter(chapter, max_length):
    divided_chapter = []
    text = chapter_to_str(chapter)
    if len(text) <= max_length:
        divided_chapter.append(text)
    else:
        subtexts = []
        subtext = ''
        sentences = text.split('. ')
        for sentence in sentences:
            if len(subtext + sentence) > max_length:
                subtexts.append(subtext)
                subtext = sentence + '. '
            else:
                subtext += sentence + '. '
        if subtext:
            subtexts.append(subtext)
        divided_chapter.extend(subtexts)
    return divided_chapter
def combine_subtexts(subtexts):
    combined_text = ''
    for i, subtext in enumerate(subtexts):
        if i == 0:
            combined_text += subtext
        else:
            # Check if the previous subtext ends with a sentence boundary
            if combined_text[-2:] == '. ' or combined_text[-2:] == '! ' or combined_text[-2:] == '? ':
                combined_text += subtext
            else:
                # If the previous subtext does not end with a sentence boundary, add one
                combined_text = combined_text.rstrip() + '. ' + subtext.lstrip()
    return combined_text

#print(BeautifulSoup(chapters_list[0].get_body_content(), 'html.parser'))

rozdzial1 = chapter_to_str(chapters_list[0])
podzielony_rozdzial1 = divide_chapter(chapters_list[0], max_length=5000)

#print(f'Normalny rozdział: {rozdzial1} \n\n\n\n--------------------ROZDZIELNIK--------------------------\n\n\n\n Podzielony rozdzial sklejony za pomocą funkcji: {combine_subtexts(podzielony_rozdzial1)}')
for subtext in podzielony_rozdzial1:
    translated = GoogleTranslator(source='english', target='polish').translate(text=subtext)
    cleaned = translated.replace('\n',' ')
    print(cleaned)
# print(f'Długość pierwszego rozdziału:{len(normal_chapters[0])} Długość pierwszych 3 elementów:{len(divided_chapters[0])+len(divided_chapters[1])+len(divided_chapters[2])}')
# print(f'Ostatnie znaki normalnego rozdziału:{normal_chapters[0][len(normal_chapters[0])-23:-1]} OStatnie znaki 3 elementu listy podzielonych rozdziałów:{divided_chapters[2][len(divided_chapters[2])-23:-1]}')


