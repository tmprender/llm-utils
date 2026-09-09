#!/bin/bash

llama-server -m ~/.models/hf/Qwen3.8-27B-Q8_0/Qwen3.8-27B-Q8_0.gguf \
  --mmproj ~/.models/hf/Qwen3.8-27B-Q8_0/mmproj-BF16.gguf \
  --port 8081 \
  --verbose

