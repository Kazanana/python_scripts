#nauka

import os
import platform
#import matplotlib.pyplot as plt
a = 35756351346243534

def sum_of_digits(number):
    sum = 0
    for i in str(number):
        sum = sum+int(i)
    if sum > 9:
        return sum_of_digits(sum)
    return sum

#print(sum_of_digits(a))

def fib(n):
    if not isinstance(n,int):
        raise TypeError("musisz podać liczbę całkowitą")
    if n <= 0:
        raise ValueError("liczba musi być dodatnia")
    if n in (1,2):
        return 1
    return fib(n-1) + fib(n-2)

# z = 25
# y = [fib(i) for i in range(1,z)]
# x = [i for i in range(1,z)]
# print(y[-1])

# #plt.plot(x,y)
# plt.plot(x,[sum_of_digits(i) for i in y], '.')
# plt.title('Ciąg fibonacciego')
# plt.show()
#print("dupa" + ",")

# string = "hello"
# reversed = ""
# def funkcja(string):
#     for char in string:




# reversed = ""

# for i in range(len(string),0,-1):
#     reversed = reversed + string[i-1]

# print(f'String: {string} Reversed: {reversed}')
# print(string[0:-1])

# import datetime

# x = datetime.datetime.now()
# print(x.strftime("%d-%m-%GT%X"))

#przygotowanie string do analizy słów
#string = "Dupa mała, dupa duża, dupa mała i duża."
# list_of_chars = [",", ".", "-", ":", "!", "?", ";"]
# clean_string = string

# for char in list_of_chars:
#     clean_string = clean_string.replace(char,"")

# clean_string = clean_string.lower()

# words_count = {}
# for word in clean_string.split():
#     if word not in words_count.keys():
#         words_count[word] = 1
#     else:
#         words_count[word] += 1

# print(words_count)

# def words_frequency(string):
#     list_of_chars = [",", ".", "-", ":", "!", "?", ";"]
    

#     for char in list_of_chars:
#         string = string.replace(char,"")
#     string = string.lower()

#     words_count = {}
#     for word in string.split():
#         if word not in words_count.keys():
#             words_count[word] = 1
#         else:
#             words_count[word] += 1

#     sorted_words_count = sorted(words_count.items(), key=lambda x:x[1], reverse=True)
#     words_count = dict(sorted_words_count)
#     return words_count

# string = "Dupa mała, dupa duża, dupa mała i duża."

# print(words_frequency(string))

#W każde zdanie stawić od 1 do 3 kurew
#podzielić na zdania
#wygenerować losową liczbę od 1 do 3
#Wybrać losowe słowo w zdaniu po którym będzie kurwa
#wstawić kurwe po danym słowie
#zlepić z powrotem w jeden string
# import random
# random.seed()

# string_czysty = """Zaczynam pisać po paru rozdziałach bo czytałem tę książkę, kończąc Education of the Will. Narrator opisuje chorobę psychiczną swojego przyjaciela Konioluba Grubasa. Opisuje go w jako trzecią osobę, ale jest to tylko zabieg literacki bo w rzeczywistości narrator i Grubas to ta sama osoba. Koniolub zaczął pogrążać się w chorobie psychicznej po tym jak otrzymał telefon od swojej przyjaciółki, że chce popełnić samobójstwo. Rozmawiał z nią o tym i powiedział parę zdań które nie pomogły wyjść jej z tej sytuacji. Po tych wydarzeniach Grubas doznał czegoś co zmieniło jego umysł. Pewnego dnia został trafiony promieniem różowego światła które napełniło go boską energią. Przez jakiś czas potrafił mówić i pisać po łacinie z którą nigdy wcześniej nie miał doczynienia. 
# W następnych rozdziałach przysłuchujemy się rozmowie przyjaciół - Kevina, narratora, Konioluba Grubasa i Sherri. Kevin jest cyniczny i stara się retoryką i różnymi sofizmatami odwieść Grubasa od swoich przekonań na temat Boga i rzeczywistości. W trakcie czytania widzę wiele ciekawych sprzeczek na tle filozoficznym i teozoficznym, ale w tym momencie nie jestem w stanie dokładnie przedstawić jakiejś. Muszę nad tym popracować. Czytając coś z czym się zgadzam i co wzbudza we mnie emocje nie zapamiętuję treści słów tylko uczucie jakie we mnie wywołały. Może dlatego mam trudności z przekazywaniem idei o których czytam. Postaram się wytłumaczyć jakiś argument z książki osobie która jej nie czytała.

# Po tym jak Grubasa opuściła żona i zabrała ze sobą syna próbował popełnić samobójstwo. Jednak pomimo zażycia dawki leków podwójnie przekraczającej śmiertelną, podcięciu sobie żył i próbie uduszenia się za pomocą spalin samochodu, Grubas został podtrzymany przy życiu i przeniesiony do szpitala psychiatrycznego. W tym ośrodku poznał doktora z którym rozpoczął rozmowę na temat swoich przekonań na temat boga. Od tej osoby usłyszał słowa które znacząco poprawiły jego stan psychiczny. “Jest Pan autorytetem”, odnosiły się do jego poglądów na temat rzeczywistości i natury tego świata. Koniolub Grubas zastanawiał się czy umysł który stworzył ten świat jest irracjonalny czy racjonalny. Po rozmowach z doktorem Stone’em dowiedział się o podejściu do tego tematu filozofii gnostycznej. Wszechświat został stworzony przez istotę irracjonalną, można by rzec złą i okrutną, lecz nad nią, powyżej jej wpływów znajduje się prawdziwy Bóg który jest racjonalny i dobry. Przedziera się on do rzeczywistości stworzonej przez tą złą istotę i objawia się w różnych postaciach ludziom. Zaznajomiwszy się odrobinę z filozofią hermetyczną dostrzegam w rozważaniach Grubasa wiele implementacji 7 praw hermetycznych. Jestem ciekawy czy wynika to z wyższości tej filozofii nad innymi i najlepszym wyabstrahowaniu praw rządzącymi tym światem, czy też przez to, że nią zainteresowałem się pierwszą w tym momencie wszystko interpretuję poprzez jej pryzmat. Dowiem się pewnie doświadczając na własnej skórze konsekwencji stosowania się do tych przekonań.

# Po opuszczeniu szpitala psychiatrycznego Grubas zamieszkał z Sherri, swoją przyjaciółką chorą na raka. Kochał ją chociaż nie odwzajemniała jego uczuć. Mówiła o tym nawet wprost. Od lat była zakochana w pastorze kościoła w którym pracowała jako osoba zajmująca się administracyjnymi sprawami. Pastor z kolei dobrze o tym wiedział i nie chciał jej uczuć adresować. Sherri miała dziwny zwyczaj nienawidzić najbardziej osób które jej pomagały i które się o nią troszczyły. Gdy była wycieńczona chorobą i przebywała u swojej siostry która się nią opiekowała wyciągneła wnioski, że jej nienawidzi, że pomimo tego, że jest zakonnicą to na pewno się puszcza. W tym rozdziale padło ciekawe stwierdzenie - rak to choroba która objawia się w osobach które chcą umrzeć. W każdym są komórki rakowe które są niszczone przez układ odpornościowy zanim zaczną wyrządzać większą szkodę. Ludzie którzy “dostają raka” podświadomie chcą umrzeć przez co deaktywują swój układ odpornościowy. Ta teza nie wyjaśnia jednak dlaczego dzieci umierają na raka. Nie posiadają jeszcze wystarczająco rozwiniętej osobowości i umysłu żeby myśleć o życiu i śmierci. Moim zdaniem może być to wyjaśnione przez osoby wokół tych młodych ludzi które myślą o ich losie. Jeśli rodzic stworzył w głowie obraz tragedii związanej ze swoją rodziną to ta zła energia może przejść na innych, może zarazić ciało drugiej osoby.

# Po jakimś czasie Sherri także opuściła Grubasa który został sam, bez celu i ambicji, pragnący śmierci. Jedyne co był w stanie robić to pisać swój traktat i egzegezę. W tej części książki zaczyna się więcej rozważań na temat tego jaki obraz świata odkrył Koniolub Grubas. Narrator także zaczął odczuwać pewne rozmywanie się rzeczywistości, śniło mu się, że mieszka w drogim domu z ogródkiem i różami wzdłuż ścian, że jego ładna i młoda żona podlewa te kwiaty i , że żyją w spokoju. Jednak na jawie narrator mieszkał sam w mieście, nie widział nawet nigdy na żywo kobiety która we śnie była jego żoną. Uświadomił sobie, że obraz jaki zobaczył może przedstawiać jego ojca i matkę w dziesięcioleciu przed jego narodzinami. To spostrzeżenie staje się podstawą do przemyśleń na temat pamięci genetycznej. Każdy człowiek posiada zapisane w genach wspomnienia całego gatunku ludzkiego jaki żył przed nim. Aby odblokować te wspomnienia trzeba ujrzeć odpowiedni symbol, teraźniejszy dla ludzi których wspomnienia chcemy ujrzeć. Rodzi to tezę o żywej informacji, braku fenomenologicznej rzeczywistości. Jesteśmy tylko umysłami postrzegającymi informacje, nieśmiertelne logos może wpływać na ten umysł przenosząc go pomiędzy różnymi czasoprzestrzeniami. 

# W kolejnym rozdziale poznajemy imię narratora - Phil. Większość przemyśleń skupia się na planie znalezienia zbawiciela przez Grubasa. Postanawia on wyruszyć w podróż aby go odnaleźć. Drogę ma mu wskazać Zebra, niewidoczny, wtapiający się w rzeczywistość Bóg. Phil zastanawiając się nad przekonaniami Grubasa dochodzi do wniosku, że każdy jest swoim własnym zbawicielem. Ciężko mi się dzisiaj pisze :/

# Po tym jak Kevin zabiera swoich przyjaciół na film pt. Valis fabuła nabiera tempa. Koniolub stwierdza, że zbawiciela powinien szukać w stanach zjednoczonych a nie w Chinach. Phil kontaktuje się z fotografem który ma kontakt do scenarzysty, reżysera i głównego aktora w filmie. Nawiązują z nim kontakt dzięki wiedzy grubasa, kazał Philowi przekazać w rozmowie hasło KING FELIX. 
#         Dowiadujemy się także o tym, że Philip po grecku oznacza osobę lubiącą konie, a Dick po niemiecku to grubas. Można więc twierdzić, że postać Konioluba Grubasa jest jedną z osobowości narratora z którym utożsamia się autor. 

# Przeczytałem już wszystkie rozdziały, został jeszcze traktat na końcu, egzegeza Konioluba, ale myślę, że czytanie jej jednym ciągiem mija się z celem. Kevin, David, Phil i Koniolub jadą do gościa który wyreżyserował film. Mieszka w okolicy słynącej z winogron razem z żoną Lindą i autorem muzyki do filmu - Minim. Mają córkę która według nich jest ucieleśnieniem Zbawiciela. Dziewczynka ma na imię Sophia - mądrość. Pomimo tego, że ma 2 lata rozmawia z nimi z niespotykaną wiedzą. Jej słowa trafiają prosto do ich dusz. Wtedy to Phil zdaje sobie sprawę, że Grubas i on to jedna osoba, łączą się w jedność. Narrator zostaje uleczony. Jednak po wyjeździe z malowniczej miejscowości
#  dowiadują się, że mała Sophia umiera, zostaje zabita przez eksperyment Miniego z laserem przekazującym informację. 
# W tym momencie książka przyspieszyła dla mnie. Narrator wrócił do konwersacji ze swoim alter ego. Grubas zaczął podróżować w poszukiwaniu Mesjasza a Phil siedział przed telewizorem i czuwał tak jak zostało mu przykazane dawno temu.
# Autor przedstawił w książce swoje duchowe przeżycia, rozważania na temat rzeczywistości. Wiele z nich było przedstawiane pod kątem ideologii i filozofii które autor poznał w trakcie życia - chrześcijaństwo, buddyzm, nawet ezoteryczne stowarzyszenia kultury zachodniej takie jak różokrzyżowcy. Ze mną rezonowały te fragmentu w których mogłem odnaleźć aspekty hermetyzmu i 7 wielkich praw. Coraz częściej widzę jak te prawa znajdują się w rzeczywistości której doświadczam.
# """
# zdania = string_czysty.split(".")
# string_koncowy = ""
# #print(zdania)
# #zdanie = zdania[0]
# for zdanie in zdania:
#     liczba_kurw = random.randrange(4)
#     if zdanie == '\n':
#         zdanie_kurwa = zdanie
#         zdanie_kurwa = zdanie_kurwa.join(".")
#         string_koncowy = string_koncowy + zdanie_kurwa
#         continue
#     elif liczba_kurw == 0:
#         zdanie_kurwa = zdanie
#         zdanie_kurwa = zdanie_kurwa.join(".")
#         string_koncowy = string_koncowy + zdanie_kurwa
#         continue
#     #print(zdanie)
#     #print(f"Liczba kurw w zdaniu: {liczba_kurw}")
#     #print(f"Początkowe zdanie:\n{zdanie}")
#     for i in range(liczba_kurw):
#         losowe_slowo = random.choice(zdanie.split())
#         slowo_poczatek = zdanie.find(losowe_slowo)
#         slowo_dlugosc = len(losowe_slowo)
#         slowo_koniec = slowo_poczatek+slowo_dlugosc
#         zdanie_kurwa = zdanie[:slowo_koniec] + " kurwa" + zdanie[slowo_koniec:]
#         zdanie_kurwa = zdanie_kurwa.join(".")

#     # print(zdanie_kurwa)
#     string_koncowy = string_koncowy + zdanie_kurwa

# print(string_koncowy)
# #print(f"Końcowe zdanie:\n{zdanie}")
# #print(zdanie[slowo_poczatek:slowo_poczatek+slowo_dlugosc])
# #print(zdanie[:slowo_koniec] + " kurwa" + zdanie[slowo_koniec:])

# import webbrowser
# path = 'file:///C:/Users/HP/books/A%20History%20of%20Central%20Banking%20and%20the%20Enslavement%20of%20Mankind%20by%20Stephen%20Goodson%20(z-lib.org).pdf'
# webbrowser.open_new(path)
# import PyPDF2

# path = '/mnt/c/Users/HP/books/A History of Central Banking and the Enslavement of Mankind by Stephen Goodson (z-lib.org).pdf'
# stalowy = '/mnt/c/Users/HP/Downloads/Skuteczne-Suplementy.-Decydujaca-Przewaga-STALOWY-SZOK.pdf'

# with open(stalowy, 'rb') as file:
#     pdfReader = PyPDF2.PdfReader(file)
#     pageObj = pdfReader.pages[0]
#     print(pdfReader)
#     # for page in pageObj:
#     #     print("---STRONA---")
#     #     print(page.extract_text())
#     #     print("---STRONA---")
# a_dict = {'color': (15), 'fruit': (16, 17), 'pet': 'dog'}
# for key in a_dict:
#     print(len(a_dict[key]))
print(platform.system())
stalowy = '/mnt/c/Users/HP/Downloads/Skuteczne-Suplementy.-Decydujaca-Przewaga-STALOWY-SZOK.pdf'
print(stalowy)

def modify_path_string(path):
    if platform.system() == "Windows":
        path = path.replace('/mnt/c', 'C:')
        path = path.replace('/', '\\')
        return path
    else:
        return path


if platform.system() == "Windows":
    stalowy = stalowy.replace('/mnt/c', 'C:')
    stalowy = stalowy.replace('/', '\\')

print(stalowy)