## kVecDb

**WIP**

_Requires a kdb+ license and ability to run q_
_Follow this link to download and setup kdb+ https://code.kx.com/q/learn/install/_
_Once kdb+ is installed and q is setup, the datastore server can be run by doing `q kVecDb.q -p <port>` in this directory_

A vector datastore implementation in kbd+/q.  
Python client and an example notebook included.

Generating embeddings in the Python client using SentenceTransformer and the open source all-MiniLM-L6-v2 model.
The datastore does not generate embeddings, it only accepts a vector of floats (embeddings) and the corresponding string to store the data.

The datastore takes care of performing a similarity operation (cosine similarity) when retrieving the data given a vector of floats (embeddings).
