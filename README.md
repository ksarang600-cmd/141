# 141 — Local Security AI for Kali

**Founder: Sarang**

141 is a menu-driven Python CLI for defensive security help and authorized testing. It loads a local GGUF language model directly into the 141 process through `llama.cpp` using `llama-cpp-python`. It does not require Ollama, a model server, a cloud API, or network access during inference. The app displays `appu` as a user label; it is not authentication. Model output is advice and is never executed. A shell command runs only when the operator explicitly enters `!<command>`.

141 is the application and inference integration. The GGUF weights are a separate open model, downloaded by the user and governed by that model's license. The example below uses Qwen3 4B GGUF; this is not a model trained by the 141 project.

The 141 application code is licensed under MIT. Review the licenses of `llama-cpp-python` and the selected model before use.

## Kali setup

### 1. Install native build tools and create a virtual environment

`llama-cpp-python` builds the llama.cpp runtime for the local machine. On Kali, install the build tools, then create an isolated Python environment:

```bash
sudo apt update
sudo apt install -y python3-venv python3-dev build-essential cmake libopenblas-dev
cd ~/141
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" pip install -r requirements.txt
```

### 2. Download a local GGUF model

The default configuration expects `models/Qwen3-4B-Q4_K_M.gguf` (about 2.5 GB). Download it from the [Qwen GGUF model repository](https://huggingface.co/Qwen/Qwen3-4B-GGUF):

```bash
python -m pip install huggingface_hub
mkdir -p models
hf download Qwen/Qwen3-4B-GGUF Qwen3-4B-Q4_K_M.gguf --local-dir models
```

Keep model weights out of Git. Check available RAM and disk space first; inference speed depends on your Kali VM's allocated CPU and memory.

To use a different GGUF file, set its path before starting 141:

```bash
export LLAMA_MODEL_PATH="$HOME/models/your-model.gguf"
```

### 3. Run 141

```bash
cd ~/141
source .venv/bin/activate
python3 141.py
```

The first chat request loads the selected model into this process. The model is not automatically downloaded by 141.

## Menu and chat commands

The main menu provides local AI chat, model status, help, and exit. In chat:

- Enter ordinary text to chat with the local model.
- `/help` lists commands.
- `/model` displays the selected GGUF file.
- `/model PATH` selects another existing local `.gguf` file for this session.
- `/clear` clears the in-memory chat history.
- `!<command>` runs a command you explicitly entered in the operating-system shell.
- `/exit` quits.

The model cannot call tools through this app, and its responses are never executed. `!` commands run with the current operating-system account's permissions. Run Kali as a normal user rather than root, and only assess systems you own or are explicitly authorized to test.

## Local data and limits

- `appu` is only a display label; anyone who can run the program can use it. Use operating-system accounts and permissions for access control.
- The GGUF file stays on disk at the path you choose. Do not commit model weights, secrets, or private data to Git.
- Chat history stays in process memory and is discarded on exit. Prompts are processed by the selected local model; 141 does not send telemetry.
- Responses can be wrong or unsafe. Verify important guidance using trusted documentation and deterministic tools.
- Local inference can be slow or fail when the VM does not have enough RAM, CPU, or disk space.

## References

- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [Qwen3 4B GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF)
- [Qwen3 model license and information](https://huggingface.co/Qwen/Qwen3-4B)
