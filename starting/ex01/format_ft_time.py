import time

#in seconds since the epoch
current_time = time.time()

f_date = time.strftime("%b %d %Y", time.localtime(current_time))

#f-string

print(f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation$")
print(f_date)
