from __future__ import print_function
import sys
import copy
import numpy as np

# fileopen
argvs = sys.argv
argc = len(argvs)
if (argc < 1):
    print("Usage: # python %s filename -> Enter -> type # of threshold") % argvs[0]
    quit()

def fastq(argv):
    list = []
    temp = []
    lines = open(argvs[1]).readlines()
    while len(lines)>0:
        for i in range(4):
            temp.append(lines.pop(0))
        list.append(copy.deepcopy(temp))
        del temp[:]
    return list

fastq = fastq(argvs[1])
#/fileopen

# dictionary
dict = {'!':33, '\"':34, '':35, '$':36, '%':37, '&':38, '\'':39, '(':40, ')':41, '*':42, '+':43, ',':44, '-':45, '.':46, '/':47, '0':48, '1':49, '2':50, '3':51, '4':52, '5':53, '6':54, '7':55, '8':56, '9':57, ':':58, ';':59, '<':60, '=':61, '>':62, '?':63, '@':64, 'A':65, 'B':66, 'C':67, 'D':68, 'E':69, 'F':70, 'G':71, 'H':72, 'I':73, 'J':74, 'K':75, 'L':76, 'M':77, 'N':78, 'O':79, 'P':80, 'Q':81, 'R':82, 'S':83, 'T':84, 'U':85, 'V':86, 'W':87, 'X':88, 'Y':89, 'Z':90, '[':91, '\\':92, ']':93, '^':94, '_':95, '`':96, 'a':97, 'b':98, 'c':99, 'd':100, 'e':101, 'f':102, 'g':103, 'h':104, 'i':105, 'j':106, 'k':107, 'l':108, 'm':109, 'n':110, 'o':111, 'p':112, 'q':113, 'r':114, 's':115, 't':116, 'u':117, 'v':118, 'w':119, 'x':120, 'y':121, 'z':122, '{':123, '|':124, '}':125, '~':126}
#/dictionary

# main
def OUTPUTtoFASTA(OUTPUT):
    for data in OUTPUT:
        print('>'+data[0], end='')
        print(data[1], end='')

temp = []
OUTPUT = []
cutscore = int(raw_input())
for data in fastq:
    for i in range(len(data[3])-1):
        temp.append(dict[data[3][i]]-33)
    quality = np.array(temp)
    quality_avg = np.average(quality)
    #print quality_avg
    if quality_avg > cutscore:
        OUTPUT.append(data)
    del temp[:]

OUTPUTtoFASTA(OUTPUT)
#/main
