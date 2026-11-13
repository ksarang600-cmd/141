#!/usr/bin/env python3
"""141 local interactive REPL shell, founded by Sarang K.

Access policy: application username ``appu``.
The password is read from PAC_PASSWORD (recommended) or prompted securely.
"""

from __future__ import annotations

import getpass
import os
import subprocess
import sys
from textwrap import dedent


LOGIN_USER = "appu"
TOOL_NAME = "141"
FOUNDER = "Sarang K"
DEFAULT_PASSWORD = "appu"  # Requested initial password; override with PAC_PASSWORD.


def authenticate() -> bool:
    print(f"{TOOL_NAME} — sign in (Founder: {FOUNDER})")
    for attempt in range(1, 4):
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ")
        expected_password = os.environ.get("PAC_PASSWORD", DEFAULT_PASSWORD)
        if username == LOGIN_USER and password == expected_password:
            return True
        remaining = 3 - attempt
        print(f"[AUTH FAILED] Invalid credentials. Attempts remaining: {remaining}")
    return False


def print_help() -> None:
    print(dedent("""\
        141 commands (Founder: Sarang K)
        --------------------------------
        /help       Show this help.
        !<command>  Run a command using the current user's PowerShell.
        /exit       Exit the REPL.
        <text>      Display the request; connect an AI backend to process it.

        Authentication: application username appu.
        Set PAC_PASSWORD in the environment to replace the initial password.
        Shell commands execute with the signed-in Windows account's permissions.
        """))


def run_shell(command: str) -> None:
    command = command.strip()
    if not command:
        print("[INPUT ERROR] Enter a command after '!'.")
        return
    try:
        completed = subprocess.run(
            ["powershell.exe", "-NoLogo", "-NoProfile", "-Command", command],
            check=False,
        )
        if completed.returncode:
            print(f"[EXIT] Command returned status {completed.returncode}.")
    except FileNotFoundError:
        print("[ERROR] powershell.exe was not found on this system.")
    except OSError as exc:
        print(f"[ERROR] Could not start command: {exc}")


def main() -> int:
    if not authenticate():
        return 1
    print(f"Welcome back, Boss! {TOOL_NAME} (Founder: {FOUNDER}) — type /help for commands.")
    while True:
        try:
        line = input("141> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[SESSION] Exiting.")
            return 0
        if not line:
            continue
        if line.casefold() in {"/exit", "exit", "quit"}:
            print("[SESSION] Exiting.")
            return 0
        if line.casefold() == "/help":
            print_help()
        elif line.startswith("!"):
            run_shell(line[1:])
        else:
            print("[REQUEST RECEIVED] No language-model backend is configured.")
            print("Connect an authorized backend to generate plans or scripts from natural language.")


if __name__ == "__main__":
    sys.exit(main())
