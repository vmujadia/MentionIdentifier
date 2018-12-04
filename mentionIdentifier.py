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
                        flag = False
                        if node.type in {'NN','NNC','NNP','NNPC','QC','JJ','QF','JJP','SYM'}:
                            if node.type!='SYM':
                                temp.append(node)
                            if node.getAttribute('drel')!= None:
                                drelr = node.getAttribute('drel').split(':')[0]
                            elif node.getAttribute('dmrel')!=None:
                                drelr = node.getAttribute('dmrel').split(':')[0]
                            if ('_' not in drelr  and node.type != 'NNPC') or node.type=='SYM':
                                if len(temp)>0:
                                        list_entity.append(temp)
                                        temp = []

        final_list_entity=[]
        for i in list_entity:
            list1=[]
            for j in i:
                if j.type in {'QC','QF'} and len(i)==1:
                    continue
                else:
                    list1.append(j)
            if len(list1)>0:
                final_list_entity.append(list1)


        for i in final_list_entity:
            for j in i:
                    print (j.lex,j.upper.upper.name,)
            print ('\n')
        return final_list_entity

obj = MentionIdentifier()
d = ssf.Document(sys.argv[1])
obj.get_potiential_entities()
