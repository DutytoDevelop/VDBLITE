import vdblite
import pickle
import numpy as np
from time import time
from uuid import uuid4
import sys
from pprint import pprint as pp



if __name__ == '__main__':
    vdb = vdblite.Vdb()
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