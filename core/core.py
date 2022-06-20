#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from click import secho
import shlex, subprocess
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Confirm
from rich.prompt import Prompt
import termux.API
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from time import sleep
from rich.__main__ import make_test_card
from rich.console import Console
console = Console()

all_colors = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
)