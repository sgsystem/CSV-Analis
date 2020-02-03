# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:15:58 2020

@author: Tsvetomir Gotsov
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np


RAW_File = '1m.xls'
data = pandas.read_csv(RAW_File,sep='\t',header = 1)
data.to_csv('temp.csv')
CSV_File = 'temp.csv'
temp_dataFrame = data
try:
    Time = pandas.read_csv(CSV_File , usecols=['Time [sec]'])
except:
    print("Greshka")
try:
    Controller_temperature = pandas.read_csv(CSV_File, usecols=['Controller | Temperature'])
except:
    print("Greshka")
try:
    Motor_temperature = pandas.read_csv(CSV_File , usecols=['Motor | Temperature'])
except:
    print("Greshka")
try:
    Controller_Current = pandas.read_csv(CSV_File , usecols=['Controller | Current (RMS)'])
except:
    print("Greshka")
try:
    Motor_RPM = pandas.read_csv(CSV_File , usecols=['Motor | Motor RPM'])
    Speed = Motor_RPM/375
except:
    print("Greshka")
try:
    Battery_BDI = pandas.read_csv(CSV_File, usecols=['Battery | BDI'])
except:
    print("Greshka")
try:
    Controller_Regeneration = pandas.read_csv(CSV_File,  usecols=['Controller | Regen'])
except:
    print("Greshka")
try:
    Battery_Keyswitch_Voltage = pandas.read_csv(CSV_File,  usecols=['Battery | Keyswitch Voltage'])
except:
    print("Greshka")
try:
    Throttle_Comand = pandas.read_csv(CSV_File,  usecols=['Inputs | Throttle Command'])
    Throttle_Speed = Throttle_Comand*0.08
except:
    print("Greshka")
try: 
    Pressure = pandas.read_csv(CSV_File,  usecols=['Inputs | Pressure'])
except:
    print("Greshka")
    

#a,*CurrentVarible = (temp_dataFrame['Controller | Current (RMS)'])
#Current_Controller = np.transpose(CurrentVarible)
#b,*CurrentDirection = (temp_dataFrame['Controller | Regen'])
#c,*Timesec = (temp_dataFrame['Time [sec]'])
#Timesec_plot = np.transpose(Timesec)
#Current_Directio_bit = np.transpose(CurrentDirection)
#Current_Directio_bit_to_str = str(Current_Directio_bit)
#
#if Current_Directio_bit_to_str == str('On'):
#    Direction = 1;
#elif Current_Directio_bit_to_str == str('Off'):
#    Direction = -1;
#
#Real_Current = Direction*Current_Controller
#Visualisation_Current = np.transpose(Real_Current)



#Transpose_Current = np.transpose(Controller_Current)
#Transpose_Controller_Regeneration = np.transpose(Controller_Regeneration)
#Transpose_Motor_RPM = np.transpose(Motor_RPM)

#Controller_Regeneration_transpose_string = Controller_Regeneration_transpose.astype('|S')
#for i in Controller_Regeneration:
#   if Controller_Regeneration_transpose[0] == 'on':
#       Controller_Regeneration_transpose[0] = 1
#    else:
#        Controller_Regeneration_transpose[0] = -1

#print(Time)
#print(Controller_temperature)
#print(Motor_temperature)
#print(Controller_Current)
#print(Motor_RPM)
#print(Battery_BDI)
#print(Controller_Regeneration)
#print(Battery_Keyswitch_Voltage)
#print(Throttle_Comand)
# Ploting

try:
    plt.figure(1)
    plt.plot(Time,Controller_temperature, label = "Controller Temperature")
    plt.plot(Time,Motor_temperature, label = "Motor Temperature")
    plt.xlabel('Time, s')
    plt.ylabel('Temperature,C')
    plt.title('Temperature vs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Temperature.png', dpi=300)
except:
    print("Nqma danni za Temperature")
try:
    plt.figure(2)
    plt.plot(Time, Controller_Current,label = "Controller Current")
    plt.xlabel('Time, s')
    plt.ylabel('Current,A')
    plt.title('Controller Current vs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Current.png', dpi=300)
except:
    print("Nqma danni za Controller Current")
try:
    plt.figure(3)
    plt.plot(Time,Battery_Keyswitch_Voltage,label = "Battery vlotgae")
    plt.xlabel('Time, s')
    plt.ylabel('Battery Voltage,V')
    plt.title('Battery Voltage vs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Battery Voltage.png', dpi=300)
except:
    print("Nqma danni za Batery Voltage")
try:
    plt.figure(4)
    plt.plot(Time, Speed,label = "Speed")
    plt.plot(Time, Throttle_Speed,label = "Throttle Speed")
    plt.xlabel('Time, s')
    plt.ylabel('Speed,km/h')
    plt.title('Speed vs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Speed.png', dpi=300)
except:
    print("Nqma danni za skorost")
try:
    plt.figure(5)
    plt.plot(Time, Battery_BDI,label = "Battery BDI")
    plt.xlabel('Time, s')
    plt.ylabel('Battery BDI, %')
    plt.title('Battery BDI vs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Battery BDI.png', dpi=300)
except:
    print("Nqma danni za BDI")

try:
    plt.figure(7)
    plt.plot(Time, Pressure,label = "Main pipe Pressure")
    plt.xlabel('Time, s')
    plt.ylabel('Pressure, bar')
    plt.title('Pressure vs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Main Pipe Pressure.png', dpi=300)
except:
    print("Няма данни за налягане")
    
try:
    plt.figure(8)
    plt.plot(Timesec_plot,Real_Current,label = "Real Current")
    plt.xlabel('Time, s')
    plt.ylabel('Current, A')
    plt.title('Real Currentvs Time') 
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.savefig('Real Current.png', dpi=300)
except:
    print("Няма данни за налягане")








