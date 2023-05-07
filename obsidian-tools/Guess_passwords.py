value = False
target = input("print target-name : ")
# target old
old_ask = input("you have Target birthday Y/n : ")
if old_ask.lower() == "y" :
    old = input("print Target birthday : ")
    # upper()
    value=(f"{target.upper()}.{old}\n")
    value+=(f"{target.upper()}{old}\n")
    value+=(f"{old}.{target.upper()}\n")
    value+=(f"{old}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{old}\n")
    value+=(f"{target.lower()}{old}\n")
    value+=(f"{old}.{target.lower()}\n")
    value+=(f"{old}{target.lower()}\n")
elif old_ask.lower() != "y" and old_ask.lower() != "n" :
    print("eror")
    exit()
# father name off target
#
father_name_ask = input("you have father name off Target Y/n : ")
if father_name_ask.lower() == "y" :
    father_name = input("print target father name : ")
    # upper()
    value+=(f"{target.upper()}.{father_name}\n")
    value+=(f"{target.upper()}{father_name}\n")
    value+=(f"{father_name}.{target.upper()}\n")
    value+=(f"{father_name}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{father_name}\n")
    value+=(f"{target.lower()}{father_name}\n")
    value+=(f"{father_name}.{target.lower()}\n")
    value+=(f"{father_name}{target.lower()}\n")
elif father_name_ask.lower() != "y" and father_name_ask.lower() != "n" :
    print("eror")
    exit()
#
# mother name off target
#
mother_name_ask = input("you have mother name off Target Y/n : ")
if mother_name_ask.lower() == "y" :
    mother_name = input("print target mother name : ")
    # upper()
    value+=(f"{target.upper()}.{mother_name}\n")
    value+=(f"{target.upper()}{mother_name}\n")
    value+=(f"{mother_name}.{target.upper()}\n")
    value+=(f"{mother_name}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{mother_name}\n")
    value+=(f"{target.lower()}{mother_name}\n")
    value+=(f"{mother_name}.{target.lower()}\n")
    value+=(f"{mother_name}{target.lower()}\n")
elif mother_name_ask.lower() != "y" and mother_name_ask.lower() != "n" :
    print("eror")
    exit()
#
# city off target
#
city_ask = input("you have city off Target Y/n : ")
if city_ask.lower() == "y" :
    city = input("print target city : ")
    # upper()
    value+=(f"{target.upper()}.{city}\n")
    value+=(f"{target.upper()}{city}\n")
    value+=(f"{city}.{target.upper()}\n")
    value+=(f"{city}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{city}\n")
    value+=(f"{target.lower()}{city}\n")
    value+=(f"{city}.{target.lower()}\n")
    value+=(f"{city}{target.lower()}\n")
elif city_ask.lower() != "y" and city_ask.lower() != "n" :
    print("eror")
    exit()
#
# country off target
#
country_ask = input("you have country off Target Y/n : ")
if country_ask.lower() == "y" :
    country = input("print target country : ")
    # upper()
    value+=(f"{target.upper()}.{country}\n")
    value+=(f"{target.upper()}{country}\n")
    value+=(f"{country}.{target.upper()}\n")
    value+=(f"{country}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{country}\n")
    value+=(f"{target.lower()}{country}\n")
    value+=(f"{country}.{target.lower()}\n")
    value+=(f"{country}{target.lower()}\n")
elif country_ask.lower() != "y" and country_ask.lower() != "n" :
    print("eror")
    exit()
#
# Girlfriend off target
#
Girlfriend_name_ask = input("you have Girlfriend name off Target Y/n : ")
if Girlfriend_name_ask.lower() == "y" :
    Girlfriend = input("print Girlfriend name off target : ")
    # upper()
    value+=(f"{target.upper()}.{Girlfriend}\n")
    value+=(f"{target.upper()}{Girlfriend}\n")
    value+=(f"{Girlfriend}.{target.upper()}\n")
    value+=(f"{Girlfriend}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{Girlfriend}\n")
    value+=(f"{target.lower()}{Girlfriend}\n")
    value+=(f"{Girlfriend}.{target.lower()}\n")
    value+=(f"{Girlfriend}{target.lower()}\n")
elif Girlfriend_name_ask.lower() != "y" and Girlfriend_name_ask.lower() != "n" :
    print("eror")
    exit()
#
# boyfriend off target
#
boyfriend_name_ask = input("you have boyfriend name off Target Y/n : ")
if boyfriend_name_ask.lower() == "y" :
    boyfriend = input("print boyfriend name off target : ")
    # upper()
    value+=(f"{target.upper()}.{boyfriend}\n")
    value+=(f"{target.upper()}{boyfriend}\n")
    value+=(f"{boyfriend}.{target.upper()}\n")
    value+=(f"{boyfriend}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{boyfriend}\n")
    value+=(f"{target.lower()}{boyfriend}\n")
    value+=(f"{boyfriend}.{target.lower()}\n")
    value+=(f"{boyfriend}{target.lower()}\n")
elif boyfriend_name_ask.lower() != "y" and boyfriend_name_ask.lower() != "n" :
    print("eror")
    exit()
#
# boyfriend off target
#
pet_name_ask = input("you have pet name off Target Y/n : ")
if pet_name_ask.lower() == "y" :
    pet = input("print pet name off target : ")
    # upper()
    value+=(f"{target.upper()}.{pet}\n")
    value+=(f"{target.upper()}{pet}\n")
    value+=(f"{pet}.{target.upper()}\n")
    value+=(f"{pet}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{pet}\n")
    value+=(f"{target.lower()}{pet}\n")
    value+=(f"{pet}.{target.lower()}\n")
    value+=(f"{pet}{target.lower()}\n")
elif pet_name_ask.lower() != "y" and pet_name_ask.lower() != "n" :
    print("eror")
    exit()
#
# other information off target
#
other_information_ask = input("you have other information off Target Y/n : ")
if other_information_ask.lower() == "y" :
    other_information = input("print target the information : ")
    # upper()
    value+=(f"{target.upper()}.{other_information}\n")
    value+=(f"{target.upper()}{other_information}\n")
    value+=(f"{other_information}.{target.upper()}\n")
    value+=(f"{other_information}{target.upper()}\n")
    # lower()
    value+=(f"{target.lower()}.{other_information}\n")
    value+=(f"{target.lower()}{other_information}\n")
    value+=(f"{other_information}.{target.lower()}\n")
    value+=(f"{other_information}{target.lower()}\n")
elif other_information_ask.lower() != "y" and other_information_ask.lower() != "n" :
    print("eror")
    exit()
#
# default other information off target
#

    # upper()
value+=(f"www.{target.upper()}\n")
value+=(f"{target.upper()}.com\n")
value+=(f"{target.upper()}.hello\n")
value+=(f"{target.upper()}hello\n")
value+=(f"{target.upper()}2023\n")
value+=(f"{target.upper()}.2023\n")
# lower()
value+=(f"www.{target.lower()}\n")
value+=(f"{target.lower()}.com\n")
value+=(f"{target.lower()}.hello\n")
value+=(f"{target.lower()}hello\n")
value+=(f"{target.lower()}2023\n")
value+=(f"{target.lower()}.2023\n")
if value == False :
    print("eror")
print(value)
