# in-memory vector similarity search
# objects and/or metadata attached to vectors

# row 1: "text info here", <<vector here>>, <<timestamp>>

# row 2: "AGI memory 1", <<vector 1 - 512d similarity>>, <<vector 2 - 2048 similarity vector>>, <<timestamps>>, <<filename>>


import pickle
import numpy as np
from time import time
from uuid import uuid4
import sys
from pprint import pprint as pp


class Vdb():
    def __init__(self):
        self.data = list()
    
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
    
    def search(self, vector, field='vector', count=5):
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



if __name__ == '__main__':
    vdb = Vdb()
    dimension = 12    # dimensions of each vector                         
    n = 200    # number of vectors                   
    np.random.seed(1)             
    db_vectors = np.random.random((n, dimension)).astype('float32')
    print(db_vectors[0])
    for vector in db_vectors:
        info = {'vector': vector, 'time': time(), 'uuid': str(uuid4())}
        vdb.add(info)
    vdb.details()
    results = vdb.search(db_vectors[10])
    pp(results)