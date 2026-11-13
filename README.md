# 141 — Local Security AI for Kali

**Founder: Sarang**

141 is a menu-driven Python CLI that uses a locally running model through [Ollama](https://ollama.com/). Its colored terminal menu offers local AI chat, model status, and help. The app sends chat requests only to `127.0.0.1:11434`; it does not use a cloud API or send telemetry. The included Ollama `Modelfile` creates a local model tag named `141` from Qwen 3 4B. This is a customized model configuration, not a foundation model trained from scratch.

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

The app starts directly and displays the configured user label `appu`. No password is requested or stored.

## Menu and chat commands

The main menu provides local AI chat, Ollama/model status, help, and exit. In AI chat:

- Enter ordinary text to chat with the local model.
- `/help` lists commands.
- `/model` shows the selected local model; `/model qwen3:4b` changes it for this session.
- `/clear` clears the in-memory chat history.
- `!<command>` runs a command you explicitly entered in the current operating-system shell.
- `/exit` quits.

The model cannot call tools through this app, and its responses are never executed. `!` commands run with the current operating-system account's permissions. Run Kali as a normal user rather than root, and only run commands on systems you own or have explicit permission to assess.

## Identity and local data

- `appu` is a display label only; it is not authentication or an access-control boundary. Anyone who can run the program can use it. Use operating-system accounts and permissions if access control is required.
- Chat history stays in process memory and is discarded on exit.
- Prompts go to the local Ollama service. Do not configure Ollama to use a remote/cloud model if you need local-only processing.

## Limits

- Responses can be wrong, incomplete, or unsafe. Verify guidance using trusted documentation and deterministic tools.
- Use active testing only in an isolated lab or on systems you own or have explicit permission to assess.
- Local inference can be slow on CPU-only hardware; model downloads require disk space and internet access.

## References

- [Ollama Linux install](https://ollama.com/download/linux)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [Ollama chat API](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion)
- [Qwen 3 model library](https://ollama.com/library/qwen3)
