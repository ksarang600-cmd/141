# 141 — Local Security AI for Kali

**Founder: Sarang**

141 is a small Python chat CLI that uses a locally running model through [Ollama](https://ollama.com/). The app sends chat requests only to `127.0.0.1:11434`; it does not use a cloud API or send telemetry. The included Ollama `Modelfile` creates a local model tag named `141` from Qwen 3 4B. This is a customized model configuration, not a foundation model trained from scratch.

The 141 application code is licensed under MIT. Ollama and the downloaded base model have separate terms; review the model license before use.

## Kali quick start

### 1. Install Ollama

Follow Ollama's official [Linux install instructions](https://ollama.com/download/linux). The official installer command shown there is:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Review the installer and use Ollama's official documentation if you prefer a manual install. Keep Ollama bound to localhost; do not expose its API to a network you do not control.

### 2. Download the base model and create local model `141`

Start the local service if your installation has not already started it:

```bash
ollama serve
```

In another terminal, from the cloned repository directory:

```bash
ollama pull qwen3:4b
ollama create 141 -f Modelfile
```

Ollama lists `qwen3:4b` at about 2.5 GB on disk; actual memory use and speed depend on your system. [Model details](https://ollama.com/library/qwen3)

### 3. Clone and launch 141

```bash
git clone https://github.com/ksarang600-cmd/141.git
cd 141
python3 141.py
```

The first launch asks you to create a password for username `appu`. Enter the password privately at the hidden prompt. 141 stores only a salted PBKDF2 hash in your user config directory, outside the clone; it does not store the plaintext password in the repository.

## Commands

- Enter ordinary text to chat with the local model.
- `/help` lists commands.
- `/model` shows the selected local model; `/model qwen3:4b` changes it for this session.
- `/clear` clears the in-memory chat history.
- `!<command>` runs a command you explicitly entered in the current operating-system shell.
- `/exit` quits.

The model cannot call tools through this app, and its responses are never executed. `!` commands run with the current operating-system account's permissions. Run Kali as a normal user rather than root, and only run commands on systems you own or have explicit permission to assess.

## Password and local data

- The current source and documentation contain no plaintext password or password hash.
- The first-run credential file is outside the clone at `~/.config/141/credentials.json` on Linux (or the user's application data directory on Windows); on Linux, 141 sets restrictive directory/file permissions.
- Chat history stays in process memory and is discarded on exit.
- Prompts go to the local Ollama service. Do not configure Ollama to use a remote/cloud model if you need local-only processing.
- If the local credential file is lost, remove it and start 141 to set a new password. Keep that file private and do not commit it.

## Limits

- Responses can be wrong, incomplete, or unsafe. Verify guidance using trusted documentation and deterministic tools.
- Use active testing only in an isolated lab or on systems you own or have explicit permission to assess.
- Local inference can be slow on CPU-only hardware; model downloads require disk space and internet access.

## References

- [Ollama Linux install](https://ollama.com/download/linux)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [Ollama chat API](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion)
- [Qwen 3 model library](https://ollama.com/library/qwen3)
