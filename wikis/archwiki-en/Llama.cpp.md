# Llama.cpp

LLM inference in C/C++.

## Installation
llama.cpp is available in the AUR:

* Install  for CPU inference.
* Install  for inference with Vulkan.
* Install  for inference with CUDA.
* Install  for inference with ROCm.

## Usage
Primary executors are  and .

## llama-cli
 is the command-line executor:

 $ llama-cli -m model.gguf

## llama-server
 launches an API server with a built-in WebUI:

 $ llama-server --host address --port port -m model.gguf

## Obtaining models
llama.cpp uses models in the GGUF format.

## Download from Hugging Face
Download models from Hugging Face using the  flag:

 $ llama-cli -hf org/model

## Manual download
Manually download models using  or :

 $ wget -c model.gguf

## Tips and tricks
## Model quantization
Quantization lowers model precision to reduce memory usage.

GGUF models use suffixes to indicate quantization level. Generally, lower numbers (e.g. Q4) use less memory but may reduce quality compared to higher numbers (e.g. Q8).

## Knowledge distillation
Knowledge distillation compresses a larger model into a smaller model by training the smaller model to follow the behaviors of the larger model.

Typically, GGUF models indicate knowledge distillation using the  denotation, where:

*  represents the smaller model.
*  represents the larger model.

## Specifying context size
llama.cpp loads the context size from the model by default, and it allocates memory for the whole context window.

Specify a lower context size in case you run out of memory.

 $ llama-cli -c 32000 -m model.gguf

## Key-value cache quantization
For further memory efficiency, you can quantize the key-value cache.

 $ llama-cli -ctk q8_0 -ctv q8_0 -m model.gguf

This, combined with a lower context size, can significantly reduce memory usage.

## Agent system
While llama-server runs a WebUI, the same endpoint also operates as an OpenAI-compatible server. It can be configured to use with coding agents like  and .

Also, recent updates have introduced built-in agent capabilities.

## Built-in tools
To enable built-in tools for filesystem operations and shell access, start llama-server with:

 $ llama-server --tools all -m model.gguf

This, combined with a reasonably strong reasoning model, can be considered as a minimal coding agent running in browser.

## Model Context Protocol servers
Other tools (e.g. web_search, fetch) can be integrated to the WebUI, given that the tools are served as MCP endpoints.

## Monitoring GPU utilization
See Graphics processing unit#Monitoring.

## Troubleshooting
## MCP requests denied by CORS policy
To use the WebUI with an MCP endpoint hosted online, enable MCP CORS proxy:

 $ llama-server --webui-mcp-proxy -m model.gguf
