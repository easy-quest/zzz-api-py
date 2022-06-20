#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

#  termux-dialog | jq .text
subprocess.Popen(['termux-dialog', '|', 'jq', '.text'])
