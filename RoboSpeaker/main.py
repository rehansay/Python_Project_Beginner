import subprocess

print("Welcome to RoboSpeaker 1.1 Created by Rehan")

while True:
    text = input("Enter what you want me to speak (type 'exit' to quit): ")

    if text.lower() == "exit":
        break

    subprocess.run([
        "powershell",
        "-Command",
        f'Add-Type -AssemblyName System.Speech; '
        f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        f'$speak.Speak("{text}")'
    ])