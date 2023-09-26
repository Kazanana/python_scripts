from bs4 import BeautifulSoup
import requests

def jobs_itpracujpl(technology, city="Warszawa", seniority="17"):
    #  et=17 -> junior
    https_address = f"https://it.pracuj.pl/?wp={city}&tt={technology}&et={seniority}&jobBoardVersion=2"
    #klasa diva z ofertą: class_="ContentBoxstyles__Wrapper-sc-11jmnka-0 jevXWE JobOfferstyles__ContentBoxWrapper-sc-1rq6ue2-0 fxOjyv OffersListingstyles__OfferWrapper-sc-17xxjbz-0 kWskaM"
    #Tytuł stanowiska: tag h3, class_="JobOfferstyles__TitleHeader-sc-1rq6ue2-4 klGMvi"
    #Nazwa firmy: class_="JobOfferstyles__CompanyNameText-sc-1rq6ue2-10 fUIqOA"
    #pensja class_="JobOfferstyles__CompanyNameText-sc-1rq6ue2-10 fUIqOA"
    #Link class_="JobOfferstyles__TitleLink-sc-1rq6ue2-6 fKNeGu"
    html_text = requests.get(https_address).text
    soup = BeautifulSoup(html_text, 'lxml')
    print(soup)
    jobs = soup.find_all('div', class_="ContentBoxstyles__Wrapper-sc-11jmnka-0 jevXWE JobOfferstyles__ContentBoxWrapper-sc-1rq6ue2-0 fxOjyv OffersListingstyles__OfferWrapper-sc-17xxjbz-0 kWskaM")
    jobs_dict = {
        "company_name" : [],
        "position_name" : [],
        "offer_link" : [],
        #"publish_date" : [],
        "salary" : []
    }

    for job in jobs:
        jobs_dict['company_name'].append(job.find_all(class_="JobOfferstyles__CompanyNameText-sc-1rq6ue2-10 fUIqOA")[0].text)
        jobs_dict['position_name'].append(job.find_all(class_="JobOfferstyles__TitleHeader-sc-1rq6ue2-4 klGMvi")[0].text)
        jobs_dict['offer_link'].append(job.find_all(class_="JobOfferstyles__TitleLink-sc-1rq6ue2-6 fKNeGu")[0].get('href'))
        #jobs_dict['publish_date'].append(job.find_all('p', class_="listing_b1nrtp6c listing_pk4iags size-caption listing_t1rst47b"))
        if len(job.find_all(class_="JobOfferstyles__CompanyNameText-sc-1rq6ue2-10 fUIqOA")) == 0:
            jobs_dict['salary'].append("Nie podali")
            continue
        jobs_dict['salary'].append(job.find_all(class_="JobOfferstyles__CompanyNameText-sc-1rq6ue2-10 fUIqOA")[0].text)
    return jobs_dict

def jobs_junior_pracujpl(key_word, radius=10, city='warszawa'):
    https_address =  f"https://www.pracuj.pl/praca/{key_word};kw/{city};wp?rd={radius}&cc=5015%2C5016&et=17"
    html_text = requests.get(https_address).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_="listing_b1evff58 listing_po9665q")

    jobs_dict = {
        "company_name" : [],
        "position_name" : [],
        "offer_link" : [],
        #"publish_date" : [],
        "salary" : []
    }

    for job in jobs:
        jobs_dict['company_name'].append(job.find_all('a')[-1].text)
        jobs_dict['position_name'].append(job.find_all('h2')[-1].text)
        jobs_dict['offer_link'].append(job.find_all('a')[0].get('href'))
        #jobs_dict['publish_date'].append(job.find_all('p', class_="listing_b1nrtp6c listing_pk4iags size-caption listing_t1rst47b"))
        if len(job.find_all('span', class_="listing_sug0jpb")) == 0:
            jobs_dict['salary'].append("Nie podali")
            continue
        jobs_dict['salary'].append(job.find_all('span', class_="listing_sug0jpb")[0].text)
    return jobs_dict

#print(jobs_itpracujpl(technology="Linux"))
jobs_info = jobs_junior_pracujpl("Linux")
#print(len(list(jobs_info.values())[0]))

for i in range(len(list(jobs_info.values())[0])):
    for key in jobs_info.keys():
        print(f"{key}: {jobs_info[key][i]}")
    print("\n")





# list_of_soups = []
# list_of_offer_info = []
# list_of_salaries = []
# for i, link in enumerate(jobs_dict['offer_link']):
#     list_of_soups.append(BeautifulSoup(requests.get(link).text, 'lxml'))
#     list_of_offer_info.append(list_of_soups[i].find_all('div', class_="offer-viewIPoRwg"))
#     list_of_salaries.append(list_of_soups[i].find_all('div', class_="offer-viewG5xQ1D"))

#Data publikacji: {jobs_dict["publish_date"][i]}

# for i in range(len(jobs_dict['company_name'])):
#     print(f'Firma: {jobs_dict["company_name"][i]}\nStanowisko: {jobs_dict["position_name"][i]}\nLink: {jobs_dict["offer_link"][i]}\n Pensja: {jobs_dict["salary"][i]}\n\n')

# for pensja in jobs_dict['salary']:
#     if len(pensja) == 0:
#         continue
#     print(pensja[0].text)


#print(job.prettify())




    