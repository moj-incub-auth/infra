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
curl http://qwen-llm-predictor.vllm-serving.svc.cluster.local/v1/completions -H "Content-Type: application/json" -d '{"model": "qwen-llm", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'
```
