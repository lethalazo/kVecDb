import numpy as np
import pandas
from qpython import qconnection
from sentence_transformers import SentenceTransformer
from typing import List

MODEL = "all-MiniLM-L6-v2"

_PUT_FUNC = "{.kvecdb.put[x;`float$y; z]}"
_FIND_FUNC = "{.kvecdb.find[`float$x]}"
_RESET_FUNC = ".kvecdb.reset[]"


class kVecDb:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connection = qconnection.QConnection(host, port)
        self.model = SentenceTransformer(MODEL)

    def put(self, data: List[str], tags: List[str]):
        if len(data) != len(tags):
            raise ValueError("Incorrect number of tags")
        embeddings = self.model.encode(data)

        for i in range(len(embeddings)):
            with self.connection as qc:
                qc(_PUT_FUNC, data[i], embeddings[i].astype(np.float64), tags)

    def find(self, data: str) -> pandas.DataFrame:
        with self.connection as qc:
            return qc(_FIND_FUNC, self.model.encode(data).astype(np.float64), pandas=True)

    def reset(self):
        with self.connection as qc:
            qc(_RESET_FUNC)
