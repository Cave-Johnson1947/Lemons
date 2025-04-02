temp = 25
sunny = True

if temp > 0 and temp < 30:
    print("The temp is good")
else:
    print("The temp is bad")

if temp <= 0 or temp >= 30:
    print("The temp is bad")
else:
    print("The temp is good")

if sunny:
    print("It is sunny outside")
else:
    print("It is cloudy")

if not sunny:
    print("It is cloudy")
else:
    print("It is sunny outside")