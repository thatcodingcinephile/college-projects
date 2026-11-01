RATES_TO_INR = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105,
}


def convert_to_inr(amount, currency):
    return amount * RATES_TO_INR[currency]


def convert_currency(amount, from_currency, to_currency):
    amount_in_inr = convert_to_inr(amount, from_currency)
    converted = amount_in_inr / RATES_TO_INR[to_currency]
    return round(converted, 2)


def read_amount():
    text = input("Amount: ").strip()

    try:
        amount = float(text)
    except ValueError:
        print("Invalid amount. Enter a number.")
        return None

    if amount < 0:
        print("Amount cannot be negative.")
        return None

    return amount


def read_currency(label):
    code = input(label + ": ").strip().upper()

    if code not in RATES_TO_INR:
        available = ", ".join(RATES_TO_INR)
        print("Unsupported currency '" + code + "'. Available: " + available)
        return None

    return code


def format_amount(amount):
    if amount == int(amount):
        return str(int(amount))
    return str(amount)


def main():
    print("=== Currency Converter ===")

    amount = read_amount()
    if amount is None:
        return

    from_currency = read_currency("From")
    if from_currency is None:
        return

    to_currency = read_currency("To")
    if to_currency is None:
        return

    result = convert_currency(amount, from_currency, to_currency)

    print(format_amount(amount) + " " + from_currency + " = " + format(result, ".2f") + " " + to_currency)


main()