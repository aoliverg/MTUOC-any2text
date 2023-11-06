#!/usr/bin/python3
#    any2text
#    Copyright (C) 2023  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import codecs
import textract
import os
import sys

def arregla(text):
    textlist=text.split("\n")
    textlist2=[]
    i=0
    for t in textlist:
        try:
            if textlist[i+1].strip()[0].isupper():
                textlist2.append(t+"@SALTPARA@")
            else:
                textlist2.append(t)
        except:
            textlist2.append(t)
        i+=1
    aux="".join(textlist2)
    aux2=aux.replace("@SALTPARA@","\n")
    return(aux2)

parser = argparse.ArgumentParser(description='A script to convert several file formats to text using textract. See available file formats and requirements at: https://textract.readthedocs.io/en/stable/')
parser.add_argument('-i','--input', action="store", dest="inputfile", help='The input file to convert.',required=True)
parser.add_argument('-f','--fixpdf', action="store_true", dest="fixpdf", help='Fix some issues in PDF conversion.',required=False)


args = parser.parse_args()
inputfile=args.inputfile
file_name, file_extension = os.path.splitext(inputfile)
fixpdf=args.fixpdf
outputfile=inputfile+".txt"

sortida=codecs.open(outputfile,"w",encoding="utf-8")
try:
    text = textract.process(inputfile).decode("utf-8")
    if fixpdf and file_extension in [".pdf",".PDF"]:
        text=arregla(text)
    for linia in text.split("\n"):
        linia=linia.rstrip()
        sortida.write(linia+"\n")
    sortida.close()
except:
    print("ERROR converting:",inputfile,sys.exc_info())

