import os
import subprocess

domains = ['binary-exploitation', 'cryptography', 'forensics', 'osint', 'reverse-engineering', 'web']

for domain in domains:
  os.chdir('../' + domain)
  for file in os.listdir(os.getcwd()):
    if (os.path.isdir(file)):
      challenge = os.getcwd() + "\\" + file
      output = subprocess.run(('ctf', 'challenge', 'install', challenge), capture_output=True)
      print(output.stdout.decode("utf-8"))