from main import People

try:
    person1_name = input("Enter your name \n")
    person2_phonenumber = input("Enter your phonenumber \n")
    person3_email = input("Enter your Email \n")
    person4_county = input("Enter your county \n")
    person5_gender = input("Enter your gender \n")
    person6_religion = input("Enter your religion \n")
    person7_password = input("Enter your password \n")
    People.create(person_name=person1_name, person_phonenumber=person2_phonenumber, person_email=person3_email,
                  person_county=person4_county, person_gender=person5_gender, person_religion=person6_religion,
                  person_password=person7_password)
    print("Person created successfully")

except:
    print("Failed to create person, use a different email")
