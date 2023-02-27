from main import People

my_person = People.select()
for ppl in my_person:
    print(ppl.person_name, ppl. person_phonenumber, ppl.person_email, ppl.person_county, ppl.person_gender, ppl.person_religion, ppl.person_password)