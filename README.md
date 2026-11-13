# 141 — Local Security AI for Kali

141 is a small Python chat CLI that uses a model running locally through [Ollama](https://ollama.com/). The Python app calls Ollama at `127.0.0.1:11434`; it has no cloud API or external telemetry. It is a wrapper around an open model, not a new model trained from scratch. Model licenses and capabilities vary, so review the selected model's license and documentation.

The 141 application code is licensed under MIT; the separately downloaded model and Ollama have their own terms.

## Kali quick start

### 1. Install Ollama

Follow Ollama's official [Linux install instructions](https://ollama.com/download/linux). The official installer command shown there is:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Review the installer and use Ollama's official documentation if you prefer a manual install. Keep Ollama bound to localhost; do not expose its API to a network you do not control.

### 2. Start Ollama and download a model

In a terminal, start the local service if your installation has not already started it:

```bash
ollama serve
```

In another terminal, download the small Qwen 3 model used by default:

```bash
ollama pull qwen3:4b
```

Ollama lists this model at about 2.5 GB on disk; actual memory use and speed depend on your system. Smaller options are available if your hardware is constrained. See the [Ollama Qwen 3 library page](https://ollama.com/library/qwen3) and check the model license before use.

### 3. Clone and launch 141

```bash
git clone https://github.com/ksarang600-cmd/141.git
cd 141
python3 141.py
```

Sign in with username `appu` and the default demo password `appu`.

## Commands

- Enter ordinary text to chat with the local model.
- `/help` lists commands.
- `/model` shows the selected model; `/model qwen3:4b` changes it for this session.
- `/clear` clears the in-memory chat history.
- `!<command>` runs a command you explicitly entered in the current operating-system shell.
- `/exit` quits.

The model cannot call tools through this app, and its responses are never executed. `!` commands do run with the current operating system account's permissions. Run Kali as a normal user rather than root, and only run commands on systems you own or are authorized to assess.

## Configuration

Use environment variables to change the password or model:

```bash
export PAC_PASSWORD='use-a-unique-strong-password'
export OLLAMA_MODEL='qwen3:4b'
python3 141.py
```

The built-in `appu` / `appu` credentials are a demonstration gate only: they are not secure access control, anyone who can read the source can see them, and the gate is not a substitute for Linux user permissions or disk encryption. Set `PAC_PASSWORD` before using the tool with other people or storing it on a shared machine.

## Limits

- Responses can be wrong, incomplete, or unsafe. Verify guidance using trusted documentation and deterministic tools.
- Use active testing only in an isolated lab or on systems you own or have explicit permission to assess.
- Chat history exists only in the running process and is discarded on exit. Prompts are sent to the local Ollama process, so do not configure Ollama to use a remote/cloud model if you need local-only processing.
- Local inference can be slow on CPU-only hardware; model downloads require disk space and internet access.

## References

- [Ollama Linux download and install](https://ollama.com/download/linux)
- [Ollama chat API](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion)
- [Ollama Qwen 3 models](https://ollama.com/library/qwen3)
