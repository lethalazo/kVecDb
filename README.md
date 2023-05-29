## kVecDb

**WIP**

A vector datastore implementation in kbd+/q.  
Python client and an example notebook included.

Generating embeddings in the Python client using SentenceTransformer and the open source all-MiniLM-L6-v2 model.
The datastore does not generate embeddings, it only accepts a vector of floats (embeddings) and the corresponding string to store the data.

The datastore takes care of performing a similarity operation (cosine similarity) when retrieving the data given a vector of floats (embeddings).
