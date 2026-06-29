# BitNet-git

bitnet-git provides the official inference framework for 1-bit Large Language Models (LLMs), based on Microsoft's bitnet.cpp. It is optimized for fast and energy-efficient inference on CPUs and GPUs using 1.58-bit quantization.

## Installation
Install the  package.

## Hardware optimization
The package automatically detects your architecture and uses the most appropriate kernels:

*x86_64: Uses TL2 (optimized Lookup Table kernel) for maximum performance.
*aarch64: Uses TL1 (optimized for ARMv8.2+).

## Global models management
To streamline your workflow, we recommend setting up a global models directory and a shell helper. This allows you to run models by name without typing full paths or URIs.

## Create the models directory
Create a standard directory in your home folder:
 $ mkdir -p ~/.local/share/bitnet/models

## Configure your shell
Add the following to your  or :

 # BitNet Models Directory
 export BITNET_MODELS_DIR="$HOME/.local/share/bitnet/models"
 # BitNet Runner Helper
 bitnet-run() {
    if [ -z "$1" ]; then
        echo "Usage: bitnet-run  return 1
    fi
    local model_name="$1"
    shift
    llama-cli -m "$BITNET_MODELS_DIR/$model_name" "$@"
    }

Reload your shell:  (or ).

## Download a model
Download a recommended model directly into your new directory:

 # Download the BitNet 2B model
 wget -P "$BITNET_MODELS_DIR" https://huggingface.co/microsoft/BitNet-b1.58-2B-4T-gguf/resolve/main/ggml-model-i2_s.gguf

## Run inference with ease
Now you can run the model simply by referencing its filename:

 bitnet-run ggml-model-i2_s.gguf -p "What are the benefits of 1-bit LLMs?" -cnv

## Options
* -m : Path to the GGUF model file.
*-p : Initial prompt for the model.
*-t : Number of CPU threads to use, e.g., .
*-temp : Control randomness, e.g. .
*-cnv: Enable conversation/chat mode.

## Serving the model via API
You can also run a local API server compatible with OpenAI's API:

 bitnet-run -m ggml-model-i2_s.gguf --port 8080

Then you can access it via http://localhost:8080.

{| class="wikitable sortable"
|+ Recommended Models (x86_64)
|-
! Model !! Parameters !! Size (GGUF) !! Description
|-
| bitnet_b1_58-large || 0.7B || ~150 MB || Blazing fast, great for testing.
|-
| BitNet-b1.58-2B-4T || 2.4B  || ~500 MB || Best overall balance for daily use.
|-
| bitnet_b1_58-3B || 3.3B || ~700 MB || High performance, slightly more capable.
|-
| Llama3-8B-1.58 || 8.0B || ~1.6 GB || High quality, requires more RAM.
|}

## Troubleshooting
Build Failures: Ensure you have [https://archlinux.org/packages/core/any/base-devel/ base-devel, cmake, and clang installed.

Model Errors: Verify the model file is a valid GGUF and resides in your $BITNET_MODELS_DIR.
