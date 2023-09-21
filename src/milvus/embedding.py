from sentence_transformers import SentenceTransformer
from numpy.typing import NDArray
from milvus.config import settings


text_embedding_model = SentenceTransformer(settings.MODEL_NAME_OR_PATH)


def text_embedding(text: str) -> NDArray:
    return text_embedding_model.encode(text, convert_to_numpy=True) # type: ignore
