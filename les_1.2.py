quan_sec = int(input())
#3671
quan_hours = quan_sec // 3600

new_sec = quan_sec % 3600

quan_min = new_sec // 60

new_sec = new_sec % 60

#print("All - ", quan_sec)
#print("Hours - ", quan_hours)
#print("Min - ", quan_min)
#print("Sec - ", new_sec)
print("{}:{}:{}".format(quan_hours, quan_min, new_sec))
