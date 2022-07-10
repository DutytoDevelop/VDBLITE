import pickle
import numpy as np
from time import time
import faiss
#from uuid import uuid4
import sys
#from pprint import pprint as pp


class Vdb():
    def __init__(self):
        self.data = list()
        self.index = None
    
    def add(self, payload):  # payload is a DICT
        self.data.append(payload)  # uuid could be in payload :) 
    
    def delete(self, field, value, firstonly=False):
        for i in self.data:
            try:
                if i[field] == value:  # if field == 'timestamp' then value might be 1657225709.8192494
                    self.data.remove(i)
                    if firstonly:
                        return
            except:
                continue
                
    def initialize_index(self,field='vector'):
        vectors = [i['vector'] for i in self.data]
        if len(vectors) != 0:
            self.index = faiss.IndexFlatL2(len(vectors))
    
    def search(self, vector, field='vector', count=5):
        
        print(self.index.is_trained)   # False
        self.index.train()  # train on the database vectors
        print(self.index.ntotal)   # 0
        self.index.add()   # add the vectors and update the index
        print(index.is_trained)  # True
        print(index.ntotal)   # 200
        
        vectors = [i['vector'] for i in self.data]
        self.index = faiss.IndexFlatL2(vectors)
        
        results = list()
        for i in self.data:
            try:
                score = np.dot(i[field], vector)
            except Exception as oops:
                print(oops)
                continue
            info = i
            info['score'] = score
            results.append(info)
        ordered = sorted(results, key=lambda d: d['score'], reverse=True)
        try:
            ordered = ordered[0:count]
            return ordered
        except:
            return ordered
    
    def purge(self):
        self.data = list()
    
    def save(self, filepath):
        with open(filepath, 'wb') as outfile:
            pickle.dump(self.data, outfile)

    def load(self, filepath):
        with open(filepath, 'wb') as infile:
            self.data = pickle.load(infile)

    def details(self):
        print('DB elements #:', len(self.data))
        print('DB size in memory:', sys.getsizeof(self.data), 'bytes')
