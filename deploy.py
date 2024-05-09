import os
import subprocess
import urllib.request
import zipfile

# Download ngrok
ngrok_url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"
ngrok_zip = "ngrok.zip"
urllib.request.urlretrieve(ngrok_url, ngrok_zip)

# Extract ngrok
with zipfile.ZipFile(ngrok_zip, "r") as zip_ref:
    zip_ref.extractall("ngrok")

# Set ngrok authentication token
ngrok_auth_token = "2gE0zQMMudaZAakwEflCtvZQKbU_6a23Cvdwq6Z7fweQQqsim"
subprocess.run(["ngrok.exe", "authtoken", ngrok_auth_token], cwd="ngrok")

# Enable TS
subprocess.run(["reg", "add", "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server", "/v", "fDenyTSConnections", "/t", "REG_DWORD", "/d", "0", "/f"])
subprocess.run(["netsh", "advfirewall", "firewall", "set", "rule", "group=\"Remote Desktop\"", "new", "enable=yes"])
subprocess.run(["reg", "add", "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp", "/v", "UserAuthentication", "/t", "REG_DWORD", "/d", "1", "/f"])

# Set local user password
subprocess.run(["net", "user", "runneradmin", "P@ssw0rd!"])

# Create Tunnel
subprocess.run(["ngrok.exe", "tcp", "3389"], cwd="ngrok")
