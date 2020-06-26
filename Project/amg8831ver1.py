import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

def Average(data3last):
    return sum(data3last) / len(data3last)

while True:
# PIXELS = []
# PIXELS = PIXELS + amg.pixels
# PIXELS.sort()
    list0 = amg.pixels[0]
    list1 = amg.pixels[1]
    list2 = amg.pixels[2]
    list3 = amg.pixels[3]
    list4 = amg.pixels[4]
    list5 = amg.pixels[5]
    list6 = amg.pixels[6]
    list7 = amg.pixels[7]
    finalList = list0 + list1 + list2 + list3 + list4 + list5 + list6 + list7
    finalList.sort()
    data3last = finalList[60:63]
    average = Average(data3last)
    print(finalList)
    print("\n")
    print("\n")
    print(data3last)
    print("Average of the list =", round(average, 1))
    print("\n")
    print("\n")
    time.sleep(1)


    # print(amg.pixels)
    # print("\n")
    # print(amg.pixels[1])
    # print("\n")
    # print("\n")
# print(PIXELS)

    # for row in amg.pixels:
    # # Pad to 1 decimal place
    # # print(["{0:.1f}".format(temp) for temp in row])
    #     print(["{0:.1f}".format(temp) for temp in row])
    #     print("")
    # print("\n")
    # time.sleep(1)