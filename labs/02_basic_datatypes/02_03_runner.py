'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

seconds = ((30 * 60) + 30)
km_per_second = ((10 * 1.6) / seconds)
km_per_hour = km_per_second * 3600
print("Answer is ", km_per_hour)