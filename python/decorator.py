# Multiple functions need the same audit behavior: log function name, start time, end time, execution duration, and exceptions. How
# would you implement this using a decorator?​

# def generate_report(user_id):​

## expensive report logic​

# return {"status": "done"}​

# ------------>

# when user calls generate_report()
# decorator starts
# record function name and start time
# execute the orginal function
# if an exception occurs, record the exception
# record end time and calculate execution duration
# print the audit log

import time
from functools import wraps
def audit_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_name = func.__name__
        print(f"Starting {func_name} at {time.ctime(start_time)}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception in {func_name}: {e}")
            raise
        finally:
            end_time = time.time()
            duration = end_time - start_time
            print(f"Ending {func_name} at {time.ctime(end_time)}")
            print(f"Execution duration: {duration:.2f} seconds")
    return wrapper
@audit_log
def generate_report(user_id):
    # Simulate expensive report logic
    time.sleep(2)  # Simulating a delay for report generation
    return {"status": "done"}
print(generate_report("user123"))    