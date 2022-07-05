import time

time=time.time()

day=time//86400
remainderDay=time%86400
hours=remainderDay//3600
remainderHours=remainderDay%3600
minutes=remainderHours//60
remainderSeconds=remainderHours%60
print(day,' Day',hours,' Hours', minutes,' Minutes',remainderSeconds,' Seconds')

