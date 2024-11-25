n = int(input())

crs_count = 1
prev_sum = 0

while 1:
    if n <= prev_sum + crs_count:
        if crs_count % 2 == 1:
            print(crs_count - (n - prev_sum - 1), '/', n - prev_sum, sep='')
            break
        else:
            print(n - prev_sum, '/', crs_count - (n - prev_sum - 1), sep='')
            break
    else:
        prev_sum += crs_count
        crs_count += 1