# OpenAI GPT-OSS-120B Cog

A Cog configuration for deploying OpenAI's GPT-OSS-120B model, a large language model with 120 billion parameters.

## Overview

This repository contains the necessary configuration files to deploy the GPT-OSS-120B model using [Cog](https://github.com/replicate/cog), which packages machine learning models in Docker containers for easy deployment.

## Hardware Requirements

- **GPU**: NVIDIA H100 (recommended by OpenAI)
- **VRAM**: Sufficient memory for 120B parameter model
- **CUDA**: 12.1 or compatible

## Files

- `cog.yaml` - Cog configuration with dependencies and environment setup
- `predict.py` - Prediction interface supporting multi-turn conversations

## Usage

The model accepts a list of messages for multi-turn conversations:

```python
messages = [
    {"role": "user", "content": "Your question here"}
]
```

## Deployment

Build and run with Cog:

```bash
cog build
cog predict -i messages='[{"role": "user", "content": "Hello!"}]'
```

Deploy to Replicate:

```bash
cog push r8.im/username/gpt-oss-120b
```