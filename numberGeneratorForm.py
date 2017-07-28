#!/usr/bin/python3

# Created by Jon Jackson (Jax24135)
# Date: 04/30/2017
# README: Generates a list of numbers in this form,
# defaults to 38 lines printing.

#---Example---#
# 1. 
# 2. 
# 3. 
# ...


outFile = open("NumberedForm.txt",'w')

LINES_TO_GENERATE = 38

LINES_TO_GENERATE += 1

#lines_to_generate = int( = int(input("How many lines should I make & number? "))
for x in range(1,LINES_TO_GENERATE):
#    line = str(x)
    outFile.write(str(x) + ". " + '\n')

# Closes the target file
outFile.close()
