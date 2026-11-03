# Currency Converter

A simple console-based currency converter written in Python 3. It converts an amount between supported currencies using exchange rates stored in a dictionary and displays the result rounded to 2 decimal places.

**PS No:** 17
**Language:** Python 3
**Concepts Used:** Functions, Conditions, Operators, Dictionaries

---

## Features

- Converts between any two supported currencies: **INR, USD, EUR, GBP**
- Stores all exchange rates in a single dictionary, so rates are easy to update
- Routes every conversion through INR
- Validates the amount (must be a number and cannot be negative)
- Validates the currency codes and lists the available ones when a code is unsupported
- Accepts currency codes in any letter case (`usd`, `USD`, `Usd`)
- Rounds every result to 2 decimal places

---

## Exchange Rates

All rates are defined relative to INR:

| Currency | Value in INR |
|----------|--------------|
| INR      | 1            |
| USD      | 83           |
| EUR      | 90           |
| GBP      | 105          |

---

## How It Works

Every conversion happens in two steps, using INR as the common base:

1. **Convert the amount to INR:** `amount x rate of the source currency`
2. **Convert from INR to the target currency:** `amount in INR / rate of the target currency`

The final value is rounded to 2 decimal places.

**Example:** converting 100 USD to EUR

```
100 USD -> 100 x 83 = 8300 INR
8300 INR -> 8300 / 90 = 92.22 EUR
```

Because every currency is converted through INR, adding a new currency only needs one new entry in the dictionary. No extra conversion logic is required.

---

## Code Structure

| Function | Purpose |
|----------|---------|
| `RATES_TO_INR` | Dictionary that stores the exchange rate of each currency in INR |
| `convert_to_inr(amount, currency)` | Converts an amount from any supported currency into INR |
| `convert_currency(amount, from_currency, to_currency)` | Converts between two currencies through INR and rounds the result to 2 decimal places |
| `read_amount()` | Reads the amount from the user and checks that it is a valid, non-negative number |
| `read_currency(label)` | Reads a currency code from the user and checks that it is supported |
| `format_amount(amount)` | Formats the amount for display, so `166.0` is shown as `166` |
| `main()` | Runs the program from start to finish |

---

## Input Validation

| Invalid Input | Message Shown |
|---------------|---------------|
| Unsupported currency code (e.g. `JPY`) | `Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP` |
| Non-numeric amount (e.g. `abc`) | `Invalid amount. Enter a number.` |
| Negative amount (e.g. `-50`) | `Amount cannot be negative.` |

---

## How to Run

1. Make sure Python 3 is installed.
2. Save the code as `currency_converter.py`.
3. Run it from the console:

```bash
python3 currency_converter.py
```

4. Enter the amount, the source currency and the target currency when prompted.

---

## Sample Runs

**Normal conversion**
```
=== Currency Converter ===
Amount: 166
From: INR
To: USD
166 INR = 2.00 USD
```

**Boundary input**
```
=== Currency Converter ===
Amount: 0
From: USD
To: INR
0 USD = 0.00 INR
```

**Invalid currency**
```
=== Currency Converter ===
Amount: 10
From: JPY
Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP
```

---

## Test Cases

| # | Input | Expected Output | Result |
|---|-------|-----------------|--------|
| 1 | 166 INR to USD | `166 INR = 2.00 USD` | Pass |
| 2 | 0 USD to INR | `0 USD = 0.00 INR` | Pass |
| 3a | From: JPY | `Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP` | Pass |
| 3b | Amount: abc | `Invalid amount. Enter a number.` | Pass |
| 3c | Amount: -50 | `Amount cannot be negative.` | Pass |
| 4a | 100 USD to EUR | `100 USD = 92.22 EUR` | Pass |
| 4b | 2 GBP to INR | `2 GBP = 210.00 INR` | Pass |
| 4c | 45 EUR to USD | `45 EUR = 48.80 USD` | Pass |

---

## Concepts Demonstrated

- **Functions:** the program is split into small functions, each with one clear job
- **Conditions:** `if` statements validate the amount and the currency codes
- **Operators:** arithmetic operators perform the conversion, and comparison operators check the input
- **Dictionaries:** the exchange rates are stored as key-value pairs and looked up by currency code

---

## Possible Improvements

- Add more currencies by adding entries to `RATES_TO_INR`
- Let the user run several conversions without restarting the program
- Load exchange rates from a file or a live API instead of fixed values

MENTOR DETAILS:
Name: Mr. Satyaprakash Sethy
Github: @SATYAPRAKASHSETHY
Role: Python Mentor/ Technical Guide
