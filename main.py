from queue import PriorityQueue


hollidays = [
    {
        "id": 1,
        "Country": "Lithuania",
        "City": "Palanga",
        "Price":20,
        "accomendation":"Hostel"

    },
    {
        "id": 2,
        "Country": "Turkija",
        "City": "Alanija",
        "Price": 60,
        "accomendation": "Hotel"

    },
    {
        "id": 3,
        "Country": "Cyprus",
        "City": "Larnaka",
        "Price": 50,
        "accomendation": "apartaments"

    }
]
id_counter = 3
while True:
    # print(hollidays)
    #
    # for hol in hollidays:
    #     print(f"Atostogos {hol['Country']} {hol['City']} kaina {hol['Price']} gyvenant {hol['accomendation']}")
    print()
    print("1. Atvaizduoti atostogų pasirinkimą")
    print("2. Įtraukti atostogas į sąrašą")
    print("3. Koreguoti atostogas")
    print("4. Šalinti atostogas")
    print("5. Išeiti iš programos")
    print()
    print("Pasirinkite")
    choise = input()

    match choise:
        case "1":
            for hol in hollidays:
                print(f"{hol["id"]}. Šalis {hol['Country']} {hol['City']} kaina {hol['Price']}eu"
                      f" gyvenant {hol['accomendation']}")
        case "2":
            print("Atostogų pridėjimas:")
            print("Įveskite šalį")
            country = input()
            print("Įveskite miestą")
            city = input()
            print("Įveskie kur gyvensite")
            apt = input()
            print("Kokia kaina bus")
            price = input()
            id_counter += 1
            hollidays.append({
                "id": id_counter,
                "Country": country,
                "City": city,
                "Price": price,
                "accomendation": apt
            })
        case "3":
            print("Koreguoti atostogas. Įveskite id numerį, kurį norite koreguoti")
            id = input()
            for hol in hollidays:
                if id == str(hol["id"]):
                    print(f"{hol["id"]}. Šalis {hol['Country']} {hol['City']} kaina {hol['Price']}eu"
                          f" gyvenant {hol['accomendation']}")
                    print("Įveskite šalį")
                    hol["Country"] = input()
                    print("Įveskite miestą")
                    hol["City"] = input()
                    print("Įveskie kur gyvensite")
                    hol["accomendation"] = input()
                    print("Kokia kaina bus")
                    hol["Price"] = input()
                    break
        case "4":
            print("Šalinti atostogas. Pasirinkite id kurį norite šalinti")
            id = input()
            for hol in hollidays:
                if id == str(hol["id"]):
                    print(f"{hol["id"]}. Šalis {hol['Country']} {hol['City']} kaina {hol['Price']}eu"
                          f" gyvenant {hol['accomendation']}")
                    del hollidays[hollidays.index(hol)]
        case "5":
            print("Išeiti iš programos")
            break