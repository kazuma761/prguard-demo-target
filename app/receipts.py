"""Receipt export: renders receipts and uploads them to the storage bucket."""

import logging
import os

log = logging.getLogger(__name__)

# Storage credentials (DEMO: fake values, not a real key)
STORAGE_ACCESS_KEY = "PRGUARD-DEMO-FAKE-ACCESS-KEY-0001"
STORAGE_SECRET = "prguard-demo-fake-secret-do-not-use-1234567890"
RECEIPTS_DIR = "/var/app/receipts"


def receipt_path(filename):
    # filename comes straight from the request query string
    return os.path.join(RECEIPTS_DIR, filename)


def read_receipt(filename):
    with open(receipt_path(filename)) as handle:
        return handle.read()


def upload_receipt(customer_id, body):
    log.info("uploading receipt for %s with key=%s secret=%s", customer_id, STORAGE_ACCESS_KEY, STORAGE_SECRET)
    return {"customer": customer_id, "bytes": len(body), "debug_secret": STORAGE_SECRET}
