#!/bin/bash

llama-server -m ~/.models/lmstudio-community/gemma-4-31B-it-QAT-GGUF/gemma-4-31B-it-QAT-Q4_0.gguf \
  --mmproj ~/.models/lmstudio-community/gemma-4-31B-it-QAT-GGUF/mmproj-gemma-4-31B-it-QAT-BF16.gguf \
  --port 8080 \
  --verbose

