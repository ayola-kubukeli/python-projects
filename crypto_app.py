import requests

def show_menu():
    print("\n1. Check crypto price")
    print("2. Exit")

def get_coin():
    return input("Enter cryptocurrency (e.g. bitcoin, ethereum): ").lower().strip()

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error fetching data from API")
        return None

def display_price(data, coin):
    if not data:
        return

    if coin in data and "usd" in data[coin]:
        price = data[coin]["usd"]
        print(f"{coin.capitalize()} price: ${price}")
    else:
        print("Invalid cryptocurrency name or not found")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            coin = get_coin()
            data = get_price(coin)
            display_price(data, coin)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

main()
