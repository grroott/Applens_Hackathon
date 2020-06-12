import gensim
from gensim.models import Word2Vec, KeyedVectors

# lst=[['hello', 'this', 'is', 'the', 'sample', 'text']]
# # sentences = gensim.models.word2vec.LineSentence("new_fol.txt")
#
# model = gensim.models.Word2Vec()
# model.build_vocab(lst, min_count=1)
# model.train(lst, epochs=model.epochs, total_examples=model.corpus_count)
model=Word2Vec.load('thousand.txt')

# print(tmp)

cv=['trichy', 'chennai', 'gokul', 'klm', 'fog', 'mist', 'cloud', 'google', 'fb']


model1=KeyedVectors.load('thousand.txt')
lstt=[['trichy', 'chennai', 'gokul', 'klm', 'fog', 'mist', 'cloud', 'google', 'fb']]

model.build_vocab(lstt, update=True)
model.train(lstt, epochs=model.epochs, total_examples=model.corpus_count)
tmp=0
for i in cv:
    t=model.wv.get_vector(i)
    tmp=tmp+t

import numpy as np
model_word_vector = np.array( tmp, dtype='f')

print(model.most_similar([model_word_vector],[],topn=20000))
print(model.most_similar(positive=cv, negative=[], topn=1))
x=model.similar_by_word('issu',topn=1000, restrict_vocab=None)
model1.build_vocab(lstt, update=True)
model1.train(lstt, epochs=model.epochs, total_examples=model.corpus_count)
# print(model.most_similar("trichy"))

# print(KeyedVectors.most_similar_to_given(self=model1,entity1=cv, entities_list=['chennai', 'issu','trichy', 'gokul', 'fb', 'klm', 'fog', 'mist', 'cloud', 'google']))
# print(KeyedVectors.model1.most_similar_to_given(entity1=['trichy','chennai']))
# print(model1.most_similar_to_given())

#
# model = Word2Vec(final_lst, size=1, window=5, min_count=1, workers=4)
# word_vectors = model.wv
# fname = get_tmpfile("vectors.kv")
# word_vectors.save(fname)
# word_vectors = KeyedVectors.load(fname, mmap='r')