'''Write Python code to create a dictionary that accepts a country name as a key and
its capital city as the value. Display the details in sorted order'''


countries_capitals = {}

while True:
    country = input("Enter the country name (or type 'stop' to finish): ")
    if country.lower() == 'stop':
        break
    capital = input(f"Enter the capital city of {country}: ")
    countries_capitals[country] = capital

    # Display the details in sorted order of country names
    sorted_countries_capitals = sorted(countries_capitals.items())
    print("Country - Capital City:")
    for country, capital in sorted_countries_capitals:
        print(f"{country}: {capital}")
