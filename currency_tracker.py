import requests
from datetime import datetime

def get_naira_rate():
    # Using a simple price API for Bitcoin to NGN as an example
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=ngn"

    print("Fetching latest market rates...")
    response = requests.get(url)
    data = response.json()

    rate = data['bitcoin']['ngn']
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"--- 💸 Market Update ({time_now}) ---")
    print(f"1 BTC = {rate:,.2f} NGN")

    # Save it to a log
    with open("rate_history.log", "a") as f:
        f.write(f"{time_now}: 1 BTC = {rate} NGN\n")

if __name__ == "__main__":
    get_naira_rate()
