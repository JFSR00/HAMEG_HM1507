from HAMEG_HM1507 import *

h = HAMEG_HM1507()
# h.timeBase("A", False, "2ms");
# h.channel(1, False, HAMEG_HM1507.CH_DC, "100mV")


timeBaseSingle = False
timeBaseDivIndex = 5
channelInv = False
channelDc = True
channelDivIndex = 5

print("q/ESC - end")
print("c - connect")
print("d - disconnect")
print("a - autoset")
print("s - time base single")
print("o - time base +")
print("p - time base -")
print("i - channel inv")
print("u - channel dc/ac")
print("y - channel voltage +")
print("x - channel voltage -")

while True:
    cmd = input()
    updateTime = False
    updateChannel = False
    if cmd == "q":
        break
    if cmd == "c":
        h.connect("/dev/ttyS0")
        updateTime = True
        updateChannel = True
    if cmd == "d":
        h.disconnect();
    if cmd == "a":
        h.autoset();
    if cmd == "s":
        timeBaseSingle = not timeBaseSingle;
        updateTime = True
    if cmd == "o":
        timeBaseDivIndex = min(timeBaseDivIndex+1, len(HAMEG_HM1507.TIME_DIVS)-1)
        updateTime = True
    if cmd == "p":
        timeBaseDivIndex = max(timeBaseDivIndex-1, 0)
        updateTime = True
    if cmd == "i":
        channelInv = not channelInv;
        updateChannel = True
    if cmd == "u":
        channelDc = not channelDc;
        updateChannel = True
    if cmd == "y":
        channelDivIndex = min(channelDivIndex+1, len(HAMEG_HM1507.V_DIVS)-1)
        updateChannel = True
    if cmd == "x":
        channelDivIndex = max(channelDivIndex-1, 0)
        updateChannel = True
    if updateTime:
        h.timeBase("A", timeBaseSingle, HAMEG_HM1507.TIME_DIVS[timeBaseDivIndex])
    if updateChannel:
        h.channel(1, channelInv, channelDc, HAMEG_HM1507.V_DIVS[channelDivIndex])
  

