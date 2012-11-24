# -*- coding: utf-8 -*-
"""
Created on Wed Dec 01 18:15:55 2010

@author: op157
"""

#Chips.dat ASCII Converter
# This will convert the binary file into ascii so it is readable in a browser

if __name__ == '__main__':
    
    # Read 
    fin = open('CHIPS.dat', 'rb')
    fout = open('full.txt', 'w')
    
    # Convert each byte to ascii (byte 0xAA --> aa)
    # NOTE: must be lowercase
    byte = fin.read(1)
    while byte != "":
        fout.write( byte.encode("hex") )
        byte = fin.read(1)
        #print "a", byte.encode("hex"), "b", str(byte)
    
    # Close the files when done
    fin.close()
    fout.close()
    
    print "Done"