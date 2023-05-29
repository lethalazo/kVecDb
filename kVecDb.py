import numpy as np
import pandas
from qpython import qconnection
from sentence_transformers import SentenceTransformer
from typing import List

MODEL = "all-MiniLM-L6-v2"

_PUT_FUNC = "{put[x;`float$y]}"
_FIND_FUNC = "{find[`float$x]}"


class kVecDb:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connection = qconnection.QConnection(host, port)
        self.model = SentenceTransformer(MODEL)

    def put(self, data: List[str]):
        embeddings = self.model.encode(data)

        for i in range(len(embeddings)):
            with self.connection as qc:
                qc(_PUT_FUNC, data[i], embeddings[i].astype(np.float64))

    def find(self, data: str) -> pandas.DataFrame:
        with self.connection as qc:
            return qc(_FIND_FUNC, self.model.encode(data).astype(np.float64), pandas=True)
