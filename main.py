import re
import time


start_time1 = time.time()
regex1 = r"(\d{2})\.(\d{2})\.(\d{4})"
regex2 = r"(\d+)\.?"

test_str = "03.27.2022"

for x in range(10000000):
    matches = re.finditer(regex1, test_str)
end_time1 = time.time()
result1 = end_time1 - start_time1

print("Result 1 completed in: {:.6f} seconds".format(result1))

start_time2 = time.time()

for x in range(10000000):
    matches = re.search(regex2, test_str)
end_time2 = time.time()
result2 = end_time2 - start_time2

print("Result 2 completed in: {:.6f} seconds".format(result2))

if result1 < result2:
    print("first regex has greater performance " + regex1)
else:
    print("second regex has greater performance " + regex2)