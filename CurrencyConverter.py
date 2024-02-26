import requests

from_currency = str(
    input("Enter The Currency You'd Like To Convert From: ")).upper()

to_currency = str(
    input("Enter The Currency You'd Like To Convert To: ")).upper()

amount = float(input("Enter The Amount Of Money: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")