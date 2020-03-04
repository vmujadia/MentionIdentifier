# -*- coding: utf-8 -*-
import collections
import codecs
import re
import ssfAPI_minimal as ssf
import random
import numpy as np
import pickle
import sys

class MentionIdentifier():
    def __init__(self):
        data='init'

    def get_child(self, node, clist):
        if len(node.childList)<=0:
            return clist
        else:
            for i in node.childList:
                if True:
                    if clist == None:
                        clist=[]
                    if i not in clist:
                        clist.append(i)
                    clist=get_child(i,clist)
            return clist

    def get__parent(self, node, ddi):
        for i in ddi:
            for j in ddi[i]:
                if j==node.parent:
                    return i

    def get_potiential_entities(self, d):
        count = 1
        list_entity = []
        coref_dic = {}
        temp=[]
        if True:
            for tree in d.nodeList :
                for chunkNode in tree.nodeList :
                    for node in chunkNode.nodeList:
                        print (node.lex)
obj = MentionIdentifier()
d = ssf.Document(sys.argv[1])
obj.get_potiential_entities(d)
