def format_date(date_string):
    formatted_date = date_string.replace('/', '-')
    return formatted_date


date = input("Enter the date in the format (dd/mm/yyyy): ")
formatted_date = format_date(date)
print("Formatted date: ", formatted_date)

