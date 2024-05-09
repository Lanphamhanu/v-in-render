import subprocess

# Download ngrok
subprocess.run(["wget", "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"])

# Extract ngrok
subprocess.run(["unzip", "ngrok-v3-stable-windows-amd64.zip"])

# Set ngrok authentication token
ngrok_auth_token = "YOUR_NGROK_AUTH_TOKEN"
subprocess.run(["./ngrok/ngrok.exe", "authtoken", ngrok_auth_token])

# Enable TS
subprocess.run(["reg", "add", "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server", "/v", "fDenyTSConnections", "/t", "REG_DWORD", "/d", "0", "/f"])
subprocess.run(["netsh", "advfirewall", "firewall", "set", "rule", "group=\"Remote Desktop\"", "new", "enable=yes"])
subprocess.run(["reg", "add", "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp", "/v", "UserAuthentication", "/t", "REG_DWORD", "/d", "1", "/f"])

# Set local user password
subprocess.run(["net", "user", "runneradmin", "P@ssw0rd!"])

# Create Tunnel
subprocess.run(["./ngrok/ngrok.exe", "tcp", "3389"])
