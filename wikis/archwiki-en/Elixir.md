# Elixir

Elixir is a dynamic, functional language designed for building scalable and maintainable applications. It leverages the Erlang virtual machine (BEAM), known for running low-latency, distributed and fault-tolerant systems, while also being successfully used in web development and the embedded software domain.

## Installation
## Single version
Install the  package. It includes Erlang, which is needed to run Elixir. The Mix package manager comes pre-installed with Elixir.

## Multiple versions
If you want to run multiple versions of Elixir and/or Erlang, these tools help with installing and managing multiple Elixir/Erlang versions:

* asdf — Elixir and Erlang,
* exenv — Elixir only,
* kerl — Erlang only,
* kiex — Elixir only.

## Configuration
Be sure to have Elixir's bin path in your  environment variable to ease development.

* Single version
:

* Multiple versions
:Please refer to the tool you used to install Elixir

In both cases, you need to find your shell profile file, and then add to the end of this file the following line reflecting the path to your Elixir installation:

  export PATH="$PATH:/path/to/elixir/bin"
