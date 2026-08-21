# A Python script uses `print()` everywhere, and the client wants logs written to a file with timestamps and error details. How would
# you improve this?​

# def process_payment(payment_id):​
# print("Processing payment", payment_id)​
# result = call_gateway(payment_id)​
# print("Gateway response", result)​
# return result​


# import logging framework
# configure logging
# log the start of payment processing
# call the payment gateway and log the response
# add exception handling


import logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def process_payment(payment_id):
    logging.info(f"Processing payment {payment_id}")
    try:
        result = call_gateway(payment_id)
        logging.info(f"Gateway response: {result}")
        return result
    except Exception as e:
        logging.error(f"Error processing payment {payment_id}: {e}")
        raise
def call_gateway(payment_id):
    if payment_id:
        logging.debug(f"Calling gateway for payment {payment_id}")
        return "Payment successful"  # Simulated gateway response
    else:
        logging.warning("Invalid payment_id provided")
        return None

process_payment("12345")