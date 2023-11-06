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

parser = argparse.ArgumentParser(description='A script to convert several file formats to text using textract. It convert all the files in one directory and stores the converted files in another directory (if the output directory does not exists, it will be created). See available file formats and requirements at: https://textract.readthedocs.io/en/stable/')
parser.add_argument('-i','--input', action="store", dest="inputdir", help='The input dir containing the files to convert.',required=True)
parser.add_argument('-o','--output', action="store", dest="outputdir", help='The output dir where the converted files will be stored. If it doesn\'t exist, it will be created',required=True)
parser.add_argument('-f','--fixpdf', action="store_true", dest="fixpdf", help='Fix some issues in PDF conversion.',required=False)


args = parser.parse_args()
inputdir=args.inputdir
outputdir=args.outputdir
isExist = os.path.exists(outputdir)
fixpdf=args.fixpdf

if not isExist:
   os.makedirs(outputdir)

for file_path in os.listdir(inputdir):
    if os.path.isfile:
        file_pathIN=os.path.join(inputdir, file_path)
        file_name, file_extension = os.path.splitext(file_path)
        file_pathOUT=os.path.join(outputdir, file_path+".txt")
        sortida=codecs.open(file_pathOUT,"w",encoding="utf-8")
        try:
            text = textract.process(file_pathIN).decode("utf-8")
        except:
            print("ERROR converting:",file_pathIN,sys.exc_info())
        if fixpdf and file_extension in [".pdf",".PDF"]:
            text=arregla(text)
        for linia in text.split("\n"):
            linia=linia.rstrip()
            sortida.write(linia+"\n")
        sortida.close()



'''
inputfile=args.inputfile
file_name, file_extension = os.path.splitext(inputfile)

outputfile=inputfile+".txt"

sortida=codecs.open(outputfile,"w",encoding="utf-8")
text = textract.process(inputfile).decode("utf-8")
if fixpdf and file_extension in [".pdf",".PDF"]:
    text=arregla(text)
for linia in text.split("\n"):
    linia=linia.rstrip()
    sortida.write(linia+"\n")
sortida.close()
'''
