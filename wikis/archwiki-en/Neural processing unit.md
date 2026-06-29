# Neural processing unit

Neural processing units (NPU) are specialized processors designed to accelerate machine learning and AI-related tasks. They are commonly integrated into modern SoCs (System-on-Chip), including those found in mobile devices, single-board computers, and some newer laptops and desktops. NPUs help offload computation from the CPU and GPU, improving performance and reducing power consumption for AI workloads.

## Installation
## AMD XDNA
The AMD XDNA-based NPU is supported via the  kernel driver, which is included in recent versions of the Linux kernel and enabled automatically.

To verify if the NPU has been detected and initialized:

 $ journalctl -kg xdna

You can also check with rocminfo:

 $ /opt/rocm/bin/rocminfo

Look for agents indicating XDNA or NPU support in the output. If properly working, an agent should list ISAs under the  entry.

## Intel NPU
The Intel NPU driver is included in the latest version of the  package.

To verify whether the system detects the NPU:

 $ journalctl -kg intel_vpu

or

 $ lspci -knnd ::1200

## List of NPU-accelerated software
*  Library for computation using data flow graphs for scalable machine learning
*  FastFlowLM (FLM) delivers an Ollama-style developer experience optimized for tile-structured NPU accelerators.
