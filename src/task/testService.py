


import sentry_sdk
from sentry_sdk import capture_exception
import time
# from sentry_sdk import capture_message

sentry_sdk.init(
    "https://6a0d73088d3f42eea1b9dcd46791d1c8@o1075757.ingest.sentry.io/6077933",
    
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def test(A, B):
    if A * 0.9 < B:
        sentry_sdk.capture_message("triangle price alert is prepared.")
    else:
        pass
    

while True:

    try:
        test(0.9, 1)
    except:
        pass
    
    time.sleep(5 * 60)

