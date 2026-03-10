# Creating ModelCars

## Download and Build

```bash
podman build -f Qwen3-Containerfile  -t quay.io/noeloc/qwen3-14b-fp8-dynamic:latest --platform linux/amd64 --build-arg=HF_TOKEN=hf_tokengoeshere --build-arg=REPO_NAME=RedHatAI/Qwen3-14B-FP8-dynamic
```

## Push to REPO

```bash
podman push quay.io/noeloc/qwen3-14b-fp8-dynamic:latest
```
