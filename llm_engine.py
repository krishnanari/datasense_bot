import subprocess
import json

def ask_llm(prompt):
    cmd = ["ollama", "run", "codellama:7b", prompt]
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output.strip()
