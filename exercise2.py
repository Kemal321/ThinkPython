#İnteractive mode de yapmaya başladık hoca öyle istiyormuş meğersem :D
start_time = (6*60 + 52)*60
easy_time = (8*60 + 15)*2
tempo_time = (7*60 + 12)*3

breakfast_hour = (start_time + easy_time + tempo_time)/(60*60)
breakfast_int_hour = int(breakfast_hour)

breakfast_minute  = (breakfast_hour - breakfast_int_hour)*60
breakfast_int_minute = int(breakfast_minute)

print('Breakfast is at {}.{}'.format(breakfast_int_hour,breakfast_int_minute))
