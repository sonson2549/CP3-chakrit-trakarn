s = float(input("distance(KM):"))
h = float(input("time(hr):"))
m = float(input("time(minutes):"))
t = ((h*60)+m)*1/60
v = s/t
print(v,"Km/h")
