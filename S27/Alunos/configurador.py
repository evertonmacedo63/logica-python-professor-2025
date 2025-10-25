import os
import json

def gerar_arquivos_config(nome_aluno):
    pasta_vscode = ".vscode"
    os.makedirs(pasta_vscode, exist_ok=True)

    # tasks.json
    tasks = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "build",
                "type": "shell",
                "command": "g++",
                "args": [
                    "-g",
                    f"{nome_aluno}.cpp",
                    "-o",
                    f"{nome_aluno}.exe"
                ],
                "group": {
                    "kind": "build",
                    "isDefault": True
                },
                "problemMatcher": ["$gcc"]
            }
        ]
    }

    # launch.json
    launch = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Debug C++",
                "type": "cppdbg",
                "request": "launch",
                "program": f"${{workspaceFolder}}/{nome_aluno}.exe",
                "args": [],
                "stopAtEntry": False,
                "cwd": "${workspaceFolder}",
                "environment": [],
                "externalConsole": True,
                "MIMode": "gdb",
                "miDebuggerPath": "C:/MinGW/bin/gdb.exe",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": True
                    }
                ],
                "preLaunchTask": "build"
            }
        ]
    }

    with open(os.path.join(pasta_vscode, "tasks.json"), "w") as f:
        json.dump(tasks, f, indent=4)

    with open(os.path.join(pasta_vscode, "launch.json"), "w") as f:
        json.dump(launch, f, indent=4)

    print(f"Arquivos gerados para {nome_aluno}: tasks.json e launch.json")

# Exemplo de uso:
gerar_arquivos_config("Amanda")