# A CPU-heavy transformation freezes the application. How would you move this work to multiprocessing?​

# def transform(record):​
# # CPU-heavy calculation​
# return record * record​
# records = list(range(10_000_000))​

#---------------------------------------

from multiprocessing import Pool

def transform(record):
    # CPU-heavy calculation
    return record * record
records = list(range(10_000_000))
if __name__ == "__main__":
    with Pool() as pool:
        results = pool.map(transform, records)
    print(results[:10]) #print first 10 results to verify 
