def get_chinese_zodiac(year):

    zodiac_animals = {
        "Rat": "Adaptable, quick-witted, resourceful, often successful in business.",
        "Ox": "Patient, diligent, reliable, strong sense of responsibility.",
        "Tiger": "Brave, courageous, ambitious, natural leaders.",
        "Rabbit": "Gentle, kind, diplomatic, enjoy peace and harmony.",
        "Dragon": "Powerful, charismatic, lucky, ambitious, inspiring.",
        "Snake": "Mysterious, wise, intuitive, creative, resourceful.",
        "Horse": "Energetic, enthusiastic, freedom-loving, independent.",
        "Goat": "Artistic, compassionate, sensitive, value relationships.",
        "Monkey": "Clever, adaptable, mischievous, enjoy challenges.",
        "Rooster": "Observant, honest, outspoken, responsible.",
        "Dog": "Loyal, trustworthy, protective, good friends.",
        "Pig": "Honest, easygoing, generous, enjoy good food and company.",
    }

    if year < 1900 or year > 2099:
        return None, None  

    start_year = 1900
    offset = year - start_year

    animal = list(zodiac_animals.keys())[offset % len(zodiac_animals)]  
    definition = zodiac_animals.get(animal, None)  

    return animal, definition

year = int(input("Enter a year: "))

animal, definition = get_chinese_zodiac(year)


if animal:  
    print(f"The Chinese zodiac animal for {year} is the {animal}.")
    if definition:
        print(f"{animal} definition: {definition}")
    else:
        print(f"Definition not found for {animal}.")
else:
    print(f"Year {year} is not within the valid range for the Chinese zodiac.")
