import tkinter
import whrp15,whrp16,whrp17,whrp_all

a = int(input("Enter 1 for 2015,2 for 2016,3 for 2017,4 for all at once:"))

if (a==1):
    whrp15.run()
if (a==2):
    whrp16.run()
if (a==3):
    whrp17.run()
if (a==4):
    whrp_all.run()
"""else:
    print("Invalid Character. Try again.")"""
    
print("Done!")
