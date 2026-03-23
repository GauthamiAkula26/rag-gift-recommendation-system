from __future__ import annotations

from functools import lru_cache
from typing import Iterable

import numpy as np

from src.config import EMBEDDING_MODEL_NAME


class EmbeddingProvider:
    def __init__(self) -> None:
        self.backend = None
        self.model = None
        self._load_backend()

    def _load_backend(self) -> None:
        try:
            from sentence_transformers import SentenceTransformer

            self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)
            self.backend = "sentence-transformers"
        except Exception:
            from sklearn.feature_extraction.text import TfidfVectorizer

            self.model = TfidfVectorizer()
            self.backend = "tfidf"

    def fit_transform(self, texts: Iterable[str]) -> np.ndarray:
        texts = list(texts)
        if self.backend == "sentence-transformers":
            return np.asarray(self.model.encode(texts, normalize_embeddings=True))
        return self.model.fit_transform(texts).toarray()

    def transform(self, texts: Iterable[str]) -> np.ndarray:
        texts = list(texts)
        if self.backend == "sentence-transformers":
            return np.asarray(self.model.encode(texts, normalize_embeddings=True))
        return self.model.transform(texts).toarray()


@lru_cache(maxsize=1)
def get_embedding_provider() -> EmbeddingProvider:
    return EmbeddingProvider()
