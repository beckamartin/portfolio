import json
import requests
import sys


def main():
    try:
        n = float(sys.argv[1])

    except IndexError:
        print("Missing command-line argument")
        sys.exit(1)

    except (ValueError, NameError):
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    except requests.RequestException:
        print("Request Exception error")
        sys.exit(1)

    # print(json.dumps(req.json(), indent=2))

    response = req.json()

    rate = response["bpi"]["USD"]["rate_float"]

    # for key in response["bpi"]["USD"]:
    #    print(key, ":", response["bpi"]["USD"][key])

    amount = n * rate

    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
