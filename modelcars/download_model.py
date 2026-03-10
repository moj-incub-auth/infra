from huggingface_hub import snapshot_download
import sys

if len(sys.argv) != 2:
    raise RuntimeError("Usage:  python download_model.py hf_model_repo_name")

(_, model_repo) = sys.argv

print(f"Model to Download {model_repo}")


# Specify the Hugging Face repository containing the model

snapshot_download(
    repo_id=model_repo,
    local_dir="/models",
    allow_patterns=["*.safetensors", "*.json", "*.txt"],
)