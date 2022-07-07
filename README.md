# Vector Database Lite (VDBLITE)

Vector Database Lite (like SQLITE but for vector search)


## Quickstart


1. Install using `pip install vdblite`
2. Run a test with the following code:

```python
import vdblite
from uuid import uuid4
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
```