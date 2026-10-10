"""Per-customer charge limits."""

MAX_CHARGE_CENTS = 500_000


def within_limit(amount_cents):
    """Return True when a single charge is under the per-charge limit."""
    return 0 < amount_cents <= MAX_CHARGE_CENTS
