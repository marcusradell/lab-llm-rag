#!/usr/bin/env python3
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(url="http://localhost:6333")

if not client.collection_exists(collection_name="demo"):
    client.create_collection(
        collection_name="demo",
        vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
    )


def main():
    response = requests.post(
        "http://localhost:11434/api/embed",
        json={"model": "mxbai-embed-large", "input": "Hello, world!"},
    )
    data = response.json()
    print(data)


if __name__ == "__main__":
    main()
