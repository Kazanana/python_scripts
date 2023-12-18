import random
random.seed()

string_czysty = "Zaczynam pisać po paru rozdziałach bo czytałem tę książkę, kończąc Education of the Will. Narrator opisuje chorobę psychiczną swojego przyjaciela Konioluba Grubasa. Opisuje go jako trzecią osobę, ale jest to tylko zabieg literacki bo w rzeczywistości narrator i Grubas to ta sama osoba. Koniolub zaczął pogrążać się w chorobie psychicznej po tym jak otrzymał telefon od swojej przyjaciółki, że chce popełnić samobójstwo. Rozmawiał z nią o tym i powiedział parę zdań które nie pomogły wyjść jej z tej sytuacji. Po tych wydarzeniach Grubas doznał czegoś co zmieniło jego umysł. Pewnego dnia został trafiony promieniem różowego światła które napełniło go boską energią. Przez jakiś czas potrafił mówić i pisać po łacinie z którą nigdy wcześniej nie miał doczynienia. "
zdania = string_czysty.split(".")
string_koncowy = ""
flaga = 1
for zdanie in zdania:
    liczba_kurw = random.randrange(4)

    if zdanie == '\n':
        string_koncowy = string_koncowy + zdanie
        flaga += 1
        continue
    elif liczba_kurw == 0:
        zdanie += "."
        string_koncowy = string_koncowy + zdanie
        flaga += 1
        continue
    
    #print(zdanie)
    #print(f"Liczba kurw w zdaniu: {liczba_kurw}")
    #print(f"Początkowe zdanie:\n{zdanie}")
    i = 0
    if zdanie.split() is None:
        flaga += 1
        continue
    while i < liczba_kurw:
        print(flaga)
        losowe_slowo = random.choice(zdanie.split())
        slowo_poczatek = zdanie.find(losowe_slowo)
        slowo_dlugosc = len(losowe_slowo)
        slowo_koniec = slowo_poczatek+slowo_dlugosc
        zdanie = zdanie[:slowo_koniec] + " kurwa" + zdanie[slowo_koniec:]
        i += 1
    flaga += 1
    # print(liczba_kurw)
    # print(zdanie)
    zdanie += "."
    string_koncowy = string_koncowy + zdanie

print(string_koncowy)


