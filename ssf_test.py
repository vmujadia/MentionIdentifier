# -*- coding: utf-8 -*-
import collections
import codecs
import re
import ssfAPI_minimal as ssf
import random
import numpy as np
import pickle
import sys

from os import listdir
from os.path import isfile, join

mypath = sys.argv[1]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for file in onlyfiles:
    _file = mypath + '/' + file

    #print ('\n\n\n\n'+_file+'\n\n\n\n\n')
    #try:
    if True:
        d = ssf.Document(_file)
        for tree in d.nodeList:
            for chunkNode in tree.nodeList:
                i = 0
                for node in chunkNode.nodeList:
                    # pos tags
                    #print (node.lex+'\t'+node.type)
                    # for morph-root
                    # print (node.lex+'\t'+str(node.morphroot))
                    # for morph-vib
                    # print (node.lex+'\t'+str(node.tamUtf))
                    # for morph-number
                    #print (node.lex+'\t'+str(node.number))
                    #print (node.lex+'\t'+str(node.person))
                    #print (node.lex+'\t'+str(node.gender))
                    #print (node.lex+'\t'+str(node.morphPOS))
                    #print (node.lex+'\t'+str(node.case))
                    if i==0:
                        print (node.lex+'\t'+'B-'+str(chunkNode.type))
                    else:
                        print (node.lex+'\t'+'I-'+str(chunkNode.type))
                    i = i + 1
            print ()
    #except:
    #    print (_file)
