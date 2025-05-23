#!/usr/bin/env python3
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

dummy_data = [
    "My name is Marcus",
    "I like Helix",
    "I like Rio",
    "I love my kids",
    "My name is Rådell",
]

client = QdrantClient(url="http://localhost:6333")

if not client.collection_exists(collection_name="demo"):
    client.create_collection(
        collection_name="demo",
        vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
    )


def main():
    for i, text in enumerate(dummy_data):
        response = requests.post(
            "http://localhost:11434/api/embed",
            json={"model": "mxbai-embed-large", "input": "Hello, world!"},
        )
        data = response.json()
        embeddings = data["embeddings"][0]
        client.upsert(
            collection_name="demo",
            wait=True,
            points=[PointStruct(id=i, vector=embeddings, payload={"text": text})],
        )


if __name__ == "__main__":
    main()
