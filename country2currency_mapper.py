#create a dict of country to currency  of 10 country ask user to enter the country name, currency, on reach 10 ask name and print the currency of that country

country2currency = {}
for i in range(10):
    country = input("Enter the country name: ")
    currency = input("Enter the currency of the country: ")
    country2currency[country] = currency

country_name = input("Enter the country name to get the currency: ")
print(country2currency[country_name])
print(country2currency)
