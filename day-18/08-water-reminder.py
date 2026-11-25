# Water Drink Remeinder Project 3 in Python

import time
import subprocess

while True:
    command = (
        "Add-Type -AssemblyName PresentationFramework; "
        "[System.Windows.MessageBox]::Show('Hey Osama! Drink some water')"
    )

    subprocess.run([
        "powershell",
        "-NoProfile",
        "-Command",
        command
    ])

    time.sleep(60 * 60)
