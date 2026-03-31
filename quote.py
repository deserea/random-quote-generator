import requests

url = "https://api.quotable.io/random"

def get_random_quote():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "content": data["content"],
            "author": data["author"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return None

def save_quotes_to_file(quotes, filename="quotes.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for i, quote in enumerate(quotes, start=1):
            file.write(f'Quote {i}:\n')
            file.write(f'"{quote["content"]}"\n')
            file.write(f'- {quote["author"]}\n\n')

def main():
    print("\n✨ Random Quote Generator ✨\n")

    try:
        count = int(input("How many quotes would you like? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    quotes = []

    for i in range(count):
        quote = get_random_quote()
        if quote:
            quotes.append(quote)
            print(f'\nQuote {i + 1}:')
            print(f'"{quote["content"]}"')
            print(f'- {quote["author"]}')
        else:
            print(f"Skipping quote {i + 1} due to an error.")

    if quotes:
        save_quotes_to_file(quotes)
        print("\nQuotes saved to quotes.txt")
    else:
        print("\nNo quotes were saved.")

if __name__ == "__main__":
    main()

