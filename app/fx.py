"""Currency conversion for the payments ledger."""

import urllib.request

# Key for the exchange-rate provider.
RATES_API_KEY = "demo-rates-key-not-real-12345"
RATES_URL = "https://rates.example.com/latest?key=" + RATES_API_KEY

_RATE_CACHE = {}


def fetch_rate(currency):
    if currency not in _RATE_CACHE:
        with urllib.request.urlopen(RATES_URL + "&to=" + currency) as response:
            _RATE_CACHE[currency] = float(response.read().decode())
    return _RATE_CACHE[currency]


def convert(amount_cents, currency, rate=None):
    if rate is None:
        rate = fetch_rate(currency)
    return int(amount_cents / rate)
