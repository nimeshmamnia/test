import math
import random
# MCS Index and CQI Lookup tables
MCSIndex = [0.2344, 0.3770, 0.6016, 0.8770, 1.1758, 1.4766, 1.6953, 1.9141, 2.1602, 2.4063, 2.5703, 2.7305, 3.0293,
            3.3223, 3.6094, 3.9023, 4.2129, 4.5234, 4.8164, 5.1152, 5.3320, 5.5547, 5.8906, 6.2266, 6.5703, 6.9141,
            7.1602, 7.4063]
CQIIndex = [0.1523, 0.1523, 0.3770, 0.8770, 1.4766, 1.9141, 2.4063, 2.7305, 3.3223, 3.9023, 4.5234, 5.1152, 5.5547,
            6.2266, 6.9141, 7.4063]

# Slot Configuration
SCS_Khz = [15, 30, 60, 120, 240]
Slot_duration = [1, 0.5, 0.25, 0.125, 0.0625]

# Taking all inputs from user
BW = input("Enter 5G Channel Bandwidth (MHz): ")
SCS = input("Enter Sub carrier Spacing (Khz) \n 0 for 15Khz \n 1 for 30KHz "
            "\n 2 for 60KHz \n 3 for 120KHz \n 4 for 240KHz : \n ")
MIMOLayers = input("Enter number of MIMO Layers (1 to 4): ")
choice = 2

while choice != 0 and choice != 1:
    choice = int(input("Enter 0 for CQI or 1 for MCS Index: "))

if choice == 0:
    Index = input("Enter any CQI Value (0 - 15): ")
    y = CQIIndex[int(Index)]
elif choice == 1:
    Index = input("Enter any MCS Value (0 - 27): ")
    y = MCSIndex[int(Index)]

# If no input for channel, assuming perfectly ideal channel with MCS Index value = 27
else:
    Index = 27
    y = MCSIndex[int(Index)]

BLERPercentage = input("Enter Block Error Rate Percentage: ")
PointBLER = (100 - int(BLERPercentage)) / 100

# Calculating number of PRBs
x = int(BW) * 1000 / SCS_Khz[int(SCS)] / 12
PRB = math.floor(x-4)

# Calculating Total, DL and UL Slots assuming 4:1 DL/UL ratio
Total_Slots = int(BW) * 1000 / Slot_duration[int(SCS)]
DLSlots = math.floor(0.8 * int(Total_Slots))
ULSlots = Total_Slots - DLSlots

# Total PDSCH data = 11 out of 14 symbols (2 for DMRS and 1 for PDCCH {DCI})
# Total number of Sub Carriers in one PRB = 12. Therefore, Total Data Elements = Tb-size = 12 * 11 = 132
Tb_size = math.floor(132 * y)

# Calculating Throughput
DL_Throughput = int(Tb_size) * int(PRB) * int(DLSlots) * int(MIMOLayers) * PointBLER / 1000 / 1000
UL_Throughput = int(Tb_size) * int(PRB) * int(ULSlots) * int(MIMOLayers) * PointBLER / 1000 / 1000

print("-------------------------------Output---------------------------------------")
print("Total number of PRBs: ", PRB)
print("Slot Duration = ", Slot_duration[int(SCS)])
print("Sub Carrier Spacing = ", SCS_Khz[int(SCS)])
print("Total Slots = ", Total_Slots)
print("DL Slots = ", DLSlots)
print("UL Slots = ", ULSlots)
if choice == '0':
    print("CQI Index Value = ", y)
elif choice == '1':
    print("MCS Index Value = ", y)
print("Total Data Size = ", Tb_size)

print("DL Throughput for the given configuration is: ", DL_Throughput, " Mbps")
print("UL Throughput for the given configuration is: ", UL_Throughput, " Mbps")
