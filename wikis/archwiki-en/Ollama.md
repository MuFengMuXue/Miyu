# Ollama

Ollama is an application which lets you run offline large language models locally.

## Installation
Install the  package, which provides a daemon, command line tool, and CPU inference.

For GPU inference:

* Install  for inference with CUDA.
* Install  for inference with ROCm.
* Install  for inference with Vulkan (experimental).

Next, enable/start . Then, verify Ollama's status:

 $ ollama --version

If it says , then the Ollama service has not been run; otherwise, the Ollama service is running and is ready to accept user requests.

Next, verify that you can run models. The following command downloads the latest 270M parameter model of Gemma 3 and returns an Ollama prompt that allows you to talk to the model:

## Usage
The Ollama executable does not provide a search interface. There is no such command as . To search for a model, you need to visit their search page.

To run a model:

 $ ollama run model

To stop a model:

 $ ollama stop model

To update a model:

 $ ollama pull model

To remove a model:

 $ ollama rm model

To view locally available models:

 $ ollama list

## Troubleshooting
## ROCm is not utilizing my AMD GPU
You may have used utilities like  to monitor the utilization of your GPU during an Ollama session, but only to notice that your GPU has not been used at all.

Without configuration, ROCm simply ignores unsupported GPUs, causing everything to be computed on CPU.

To work this around, create a drop-in file for :

Where  is dependent to the GFX version that is shipped with your system.

To determine which GFX version to use, first make sure  has already been installed. It should be pulled in to your system as a dependency of , which is itself a dependency of .

Next, query the actual GFX version of your system:

 $ /opt/rocm/bin/rocminfo | grep amdhsa

You need to remember the digits printed after the word , because this is the actual GFX version of your system. The digits are interpreted as follows:

* If the digits are 4-digit, they are interpreted as , where the first two digits are interpreted as the  part.
* If the digits are 3-digit, they are interpreted as .

Then, find all installed  kernels:

 $ find /opt/rocm/lib/rocblas/library -name 'Kernels.so-*'

You need to set  to one of the available versions listed there. The rules are summarized as follows:

# For the  part, it must be strictly equal to the actual version.
# For the  part, mismatch is allowed, but it must be no greater than the actual version.
# For the  part, mismatch is allowed, but it must be no greater than the actual version.

After setting the correct , perform a daemon-reload and restart .

Then, run your model as usual. You may wish to monitor GPU utilization with  again.

## Models are not removed after uninstalling Ollama
You can manually remove the model files. They are stored in .
