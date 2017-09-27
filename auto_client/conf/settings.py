import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

PLUGIN_ITEMS = {
    "nic": "src.plugins.nic.Nic",
    "disk": "src.plugins.disk.Disk",
    "board": "src.plugins.board.Board",
    "basic": "src.plugins.basic.Basic",
    "memory": "src.plugins.memory.Memory",
}

API = "http://127.0.0.1:8866/api/server.html"

TEST = True

# MODE = "AGENT"
MODE = "SSH"
SSH_USER = "root"
SSH_POST = 22
SSH_PWD = "root"
