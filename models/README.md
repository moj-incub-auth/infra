# Testing the models

## Embeddings

```bash
curl -X POST http://qwen3-embedding-predictor.vllm-serving.svc.cluster.local/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-embedding",
    "input": [
      "First sentence",
      "Second sentence",
      "Third sentence"
    ]
  }'
```

## Text Generation

```bash
curl http://qwen3-14b-llm-predictor.vllm-serving.svc.cluster.local/v1/completions -H "Content-Type: application/json" -d '{"model": "qwen3-14b-llm", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
```

## ReRanking

```bash
curl -s http://qwen3-ranker-predictor.vllm-serving.svc.cluster.local/v1/rerank -H "Content-Type: application/json" -d '{
    "model": "qwen3-ranker",
    "query": "What is machine learning?",
    "documents": [
        "Machine learning is a subset of artificial intelligence.",
        "Python is a programming language.",
        "Deep learning uses neural networks."
    ]
}'
```