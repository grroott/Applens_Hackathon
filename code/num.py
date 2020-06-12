import numpy as np
import gensim
from gensim.models import Word2Vec, KeyedVectors
x=(np.ndarray(shape=(100,0), dtype=float, order='F'))
print(x)

model1=Word2Vec.load('thousand_sample_cbow_v2')
lst=['gokul','issu','need', 's', 'upload', 'setup', 'popul', 'other']
ls=['go']
# print(model1.similarity(lst, ''))
print(model1.most_similar(positive=lst, negative=[]))
# print(model1.wmdistance(lst, document1=1))