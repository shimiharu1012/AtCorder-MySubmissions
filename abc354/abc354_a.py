H=int(input())
plant_h=0
day=0
while True:
    # morning
    if plant_h>H:
        print(day)
        break
    # evening
    plant_h+=2**day
    day+=1
    

