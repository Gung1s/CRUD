
hollidays = [
    {
        "Country": "Lithuania",
        "City": "Palanga",
        "Price":20,
        "accomendation":"Hostel"

    },
    {
        "Country": "Turkija",
        "City": "Alanija",
        "Price": 60,
        "accomendation": "Hotel"

    },
    {
        "Country": "Cyprus",
        "City": "Larnaka",
        "Price": 50,
        "accomendation": "apartaments"

    }
]

print(hollidays)

for hol in hollidays:
    print(f"Atostogos {hol['Country']} {hol['City']} kaina {hol['Price']} gyvenant {hol['accomendation']}")
