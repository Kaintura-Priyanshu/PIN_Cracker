#!/bin/bash
# Setup script for Android Brute Force Tool
# Makes android_brute_force.py executable and installs dependencies

echo "=========================================="
echo "Android Brute Force Tool - Setup"
echo "=========================================="

# Check if ADB is installed
if ! command -v adb &> /dev/null; then
    echo "[*] Installing ADB..."
    sudo apt-get update
    sudo apt-get install -y adb
else
    echo "[+] ADB is already installed"
fi

# Make android_brute_force.py executable
chmod +x android_brute_force.py

# Create symlink for easy access
sudo ln -sf $(pwd)/android_brute_force.py /usr/local/bin/android-brute-force

echo ""
echo "[+] Setup complete!"
echo "[*] Run: python3 android_brute_force.py"
echo "[*] Or: android-brute-force"
echo ""
echo "[!] Remember: Only test devices you own!"