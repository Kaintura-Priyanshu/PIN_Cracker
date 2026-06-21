# Android PIN Brute Force Tool

A professional security testing tool for authorized penetration testing of Android devices. This tool tests the security of Android PIN locks through USB debugging.

---

## IMPORTANT LEGAL NOTICE

**READ THIS BEFORE USING THE TOOL:**

- ✅ **ONLY** use on devices you **OWN** or have **EXPLICIT WRITTEN PERMISSION** to test
- ❌ **NEVER** use on devices you don't own
- ❌ **NEVER** use for malicious purposes
- ❌ **NEVER** use to access someone else's private data
-  Unauthorized access is **ILLEGAL** and carries severe penalties
-  Law enforcement takes unauthorized access seriously
-  Always document your authorization before testing

**By using this tool, you agree to:**
1. Use it responsibly and legally
2. Accept full responsibility for your actions
3. Comply with all applicable laws
4. Not hold the author liable for misuse

---

##  Features

- ✅ Brute force testing for 4-6 digit PIN codes
- ✅ ADB-based communication with Android devices
- ✅ Real-time progress tracking with percentage
- ✅ Configurable delay between attempts (prevents lockout)
- ✅ Graceful interruption handling (Ctrl+C)
- ✅ Clean, readable output with progress indicators
- ✅ Minimal dependencies (uses Python standard library)
- ✅ Cross-platform (Linux, macOS, Windows)
- ✅ Kali Linux optimized
- ✅ No root access required
- ✅ Safe testing parameters

---

##  Requirements

### System Requirements

| Requirement | Details |
|------------|---------|
| **OS** | Linux (Kali recommended), macOS, Windows |
| **Python** | Version 3.6 or higher |
| **ADB** | Android Debug Bridge (must be installed) |
| **Android Device** | USB Debugging must be enabled |
| **USB Cable** | Data transfer capable cable |

### Android Device Setup

1. Enable **Developer Options**:
   - Go to `Settings` > `About Phone`
   - Tap `Build Number` 7 times
2. Enable **USB Debugging**:
   - Go to `Settings` > `Developer Options`
   - Toggle `USB Debugging` ON
3. Connect device via USB
4. Accept RSA fingerprint when prompted

---

## Quick Installation

### For Kali Linux (Recommended)

```bash
# Clone the repository
git clone https://github.com/Kaintura-Priyanshu/PIN_Cracker.git
cd android-brute-force

# Make setup script executable
chmod +x setup.sh

# Run setup script
./setup.sh

# Verify installation
adb devices
python3 android_brute_force.py
```

### For Other Linux Distributions

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install adb python3

# Clone and setup
git clone https://github.com/Kaintura-Priyanshu/PIN_Cracker.git
cd android-brute-force
chmod +x android_brute_force.py
```

### For macOS

```bash
# Install dependencies
brew install android-platform-tools python3

# Clone and setup
git clone https://github.com/Kaintura-Priyanshu/PIN_Cracker.git
cd android-brute-force
chmod +x android_brute_force.py
```

### For Windows

```bash
# Download ADB from:
# https://developer.android.com/studio/releases/platform-tools

# Extract and add to PATH
# Then clone and run:
git clone https://github.com/Kaintura-Priyanshu/PIN_Cracker.git
cd android-brute-force
python android_brute_force.py
```

---

## Detailed Setup Guide

### Step 1: Install ADB

```bash
# Kali Linux / Debian / Ubuntu
sudo apt-get update
sudo apt-get install adb
sudo apt-get install android-tools-adb

# Fedora / RHEL
sudo dnf install android-tools

# Arch Linux
sudo pacman -S android-tools

# macOS
brew install android-platform-tools
```

### Step 2: Verify ADB Installation

```bash
# Check ADB version
adb --version

# List connected devices
adb devices

# Should show your device
# List of devices attached
# ABC123456789    device
```

### Step 3: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/Kaintura-Priyanshu/PIN_Cracker.git
cd android-brute-force

# Or if you have the files locally
cd /path/to/android-brute-force
```

### Step 4: Make Script Executable

```bash
# Make the Python script executable
chmod +x android_brute_force.py

# Verify
ls -l android_brute_force.py
# Should show: -rwxr-xr-x
```

### Step 5: Test Device Connection

```bash
# Check if device is detected
adb devices

# If device shows as "unauthorized":
# Check your Android device and accept the RSA fingerprint

# If device shows as "offline":
# Reconnect USB cable or restart ADB
adb kill-server
adb start-server
adb devices
```

---

## How to Use

### Interactive Mode (Recommended)

```bash
# Run the script
python3 android_brute_force.py

# Or using the shortcut (if setup.sh was run)
android-brute-force
```

### Step-by-Step Walkthrough

```bash
$ python3 android_brute_force.py

==========================================================
Android PIN Brute Force Tool
==========================================================

[!] Only use on devices you own or have permission to test

Do you have permission? (y/N): y

[*] Checking connection...
[+] Device connected

[?] PIN length (4-6): 4

[?] Delay in seconds (1-5): 2

[*] Starting... Press Ctrl+C to stop

[+] Testing 4-digit PIN (Total: 10000)
[*] Progress: 10.0% (1000/10000)
[*] Progress: 20.0% (2000/10000)
[*] Progress: 30.0% (3000/10000)
[*] Trying: 1234
[+] Found: 1234

==========================================================
RESULTS
==========================================================
[+] Password: 1234
[+] Attempts: 3001
[+] Time: 100.5 seconds

[+] Done
```

### What Happens During Testing

1. **Screen Wake**: Device screen is woken up
2. **Screen Unlock**: Swipe up to access PIN input
3. **PIN Entry**: Each PIN is entered automatically
4. **Submit**: PIN is submitted with Enter key
5. **Check**: Tool checks if screen is still locked
6. **Repeat**: Process continues until PIN found

---

## Command Examples

### Basic Usage

```bash
# Start interactive mode
python3 android_brute_force.py

# Run with shortcut (after setup)
android-brute-force
```

### Verification Commands

```bash
# Check ADB connection
adb devices

# Restart ADB if needed
adb kill-server
adb start-server

# Check Python version
python3 --version

# Check script syntax
python3 -m py_compile android_brute_force.py
```

---

## ⏱️ Time Estimates

### Estimated Time for Different PIN Lengths

| PIN Length | Total Combinations | Time (2s delay) | Time (1s delay) | Time (0.5s delay) |
|------------|-------------------|-----------------|-----------------|-------------------|
| **4-digit** | 10,000 | ~5.5 hours | ~2.8 hours | ~1.4 hours |
| **5-digit** | 100,000 | ~55 hours | ~28 hours | ~14 hours |
| **6-digit** | 1,000,000 | ~23 days | ~11 days | ~5.8 days |

### Factors Affecting Time

- Delay between attempts (higher = safer)
- Device processing speed
- USB connection speed
- Screen unlock response time
- Device lockout policies

### Safe Testing Recommendations

```bash
# Recommended delays for safe testing
# 4-digit PIN: 1-2 seconds delay
# 5-digit PIN: 2-3 seconds delay  
# 6-digit PIN: 3-5 seconds delay

# Always use longer delays for production devices
# to avoid triggering lockout mechanisms
```

---

## Security Features

### Built-in Safety Measures

1. **Configurable Delays**: Prevent triggering lockout
2. **Graceful Exit**: Ctrl+C safely stops the process
3. **Progress Tracking**: Know exactly where you are
4. **Clean Up**: Restores device state after testing
5. **No Root Access**: Safe, non-privileged operation
6. **No Exploits**: Uses standard ADB interface

### Device Lockout Protection

Android devices have security features to prevent brute force:

| Failed Attempts | Action |
|----------------|--------|
| 5 attempts | 30-second delay |
| 10 attempts | 1-minute delay |
| 15 attempts | 5-minute delay |
| 20 attempts | Device wipe (optional) |

The tool respects these by using **configurable delays**.

### Best Practices for Secure Testing

```bash
# Always use safe delays
# Recommended: 2-5 seconds between attempts

# Monitor device behavior
# Stop immediately if device shows unusual behavior

# Test in isolated environment
# Use dedicated test devices when possible

# Document your testing
# Keep logs of all attempts and results
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Device Not Found

```bash
# Symptom: "[-] No device found"
# Solution:
adb kill-server
adb start-server
adb devices

# Check USB connection
# Try different USB cable
# Try different USB port
# Enable USB debugging again
```

#### Issue 2: Device Unauthorized

```bash
# Symptom: Device shows "unauthorized" in adb devices
# Solution:
# 1. Disconnect USB
# 2. Revoke USB debugging authorizations:
#    Settings > Developer Options > Revoke USB debugging authorizations
# 3. Reconnect USB
# 4. Accept RSA fingerprint on device
```

#### Issue 3: ADB Not Found

```bash
# Symptom: "[-] ADB not found"
# Solution on Kali:
sudo apt-get install adb

# Solution on macOS:
brew install android-platform-tools

# Solution on Windows:
# Add platform-tools folder to PATH environment variable
```

#### Issue 4: Permission Denied

```bash
# Symptom: "Permission denied" when running script
# Solution:
chmod +x android_brute_force.py

# Or run with Python directly:
python3 android_brute_force.py
```

#### Issue 5: Device Offline

```bash
# Symptom: Device shows "offline" in adb devices
# Solution:
adb kill-server
adb start-server
adb devices

# Reconnect USB cable
# Restart Android device
```

#### Issue 6: Screen Not Unlocking

```bash
# Symptom: Passwords not being entered correctly
# Solution:
# Manual unlock screen first
# Disable screen lock temporarily
# Check if device has custom lock screen
```

### Complete Troubleshooting Flow

```bash
# Step 1: Check ADB
adb version

# Step 2: Check device
adb devices

# Step 3: Restart ADB if needed
adb kill-server
adb start-server

# Step 4: Check device again
adb devices

# Step 5: Test basic ADB command
adb shell echo "test"

# Step 6: Run the tool
python3 android_brute_force.py
```

---

## Ethical Guidelines

### ✅ DO's

- ✅ Use only on devices you own
- ✅ Get written permission before testing
- ✅ Use in controlled, isolated environments
- ✅ Document all testing activities
- ✅ Report vulnerabilities responsibly
- ✅ Follow responsible disclosure practices
- ✅ Respect privacy and data protection laws
- ✅ Use safe delays to prevent lockout
- ✅ Stop testing if device shows unusual behavior
- ✅ Clean up after testing

### ❌ DON'Ts

- ❌ Don't test devices you don't own
- ❌ Don't test without explicit permission
- ❌ Don't use for malicious purposes
- ❌ Don't share found passwords
- ❌ Don't bypass security measures
- ❌ Don't use aggressive testing parameters
- ❌ Don't test in production environments
- ❌ Don't ignore device lockout warnings
- ❌ Don't violate data protection laws
- ❌ Don't claim false authorization

### Legal Compliance Checklist

- [ ] Written permission obtained
- [ ] Testing scope defined
- [ ] Data handling procedures in place
- [ ] Compliance with local laws verified
- [ ] Emergency procedures established
- [ ] Authorization documented
- [ ] Testing time window agreed
- [ ] Reporting format defined
- [ ] Cleanup procedures ready
- [ ] Liability acknowledged

---

## ❓ FAQ

### Q1: Is this tool legal?

**A:** The tool itself is legal for security testing purposes. However, using it on devices you don't own or without permission is illegal. Always get proper authorization.

### Q2: Can this unlock any Android phone?

**A:** No. This tool tests PIN security on devices with USB debugging enabled. It cannot bypass security on devices without USB debugging or with advanced security features.

### Q3: How long does brute forcing take?

**A:** Depends on PIN length and delay:
- 4-digit: 1-5 hours
- 5-digit: 10-55 hours
- 6-digit: 5-23 days

### Q4: Will this trigger device lockout?

**A:** With proper delays (2-5 seconds), the tool attempts to avoid lockout. However, Android's security measures may still trigger after multiple attempts.

### Q5: Can this be used on locked phones?

**A:** Only if USB debugging was already enabled before the phone was locked. This is typically not possible on locked phones.

### Q6: Does this require root?

**A:** No. The tool uses standard ADB commands and doesn't require root access.

### Q7: Can this crack alphanumeric passwords?

**A:** The basic version supports numeric PINs. Advanced versions can be modified for alphanumeric, but it would take significantly longer.

### Q8: What if the device has a time lockout?

**A:** The tool respects lockout by using configurable delays. You should increase the delay to avoid triggering lockout.

### Q9: Is this detected by antivirus?

**A:** The Python script is not malicious but may be flagged by security software due to its purpose. This is normal for security tools.

### Q10: Can I resume an interrupted brute force?

**A:** Currently, the tool starts from the beginning. Future versions may support resume functionality.

---

## Disclaimer

```
THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR 
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.

THE USER ASSUMES ALL RESPONSIBILITY FOR THE USE OF THIS TOOL.
THE AUTHOR DOES NOT CONDONE OR SUPPORT ILLEGAL ACTIVITIES.
```

---

### Code Standards

- Follow Python PEP 8 style guide
- Add comments for complex code
- Update documentation
- Test on multiple platforms
- Maintain backward compatibility

---

## ⭐ Star the Project

If you find this tool useful for security testing, please star the repository on GitHub!

---

## ⚠️ FINAL WARNING

**THIS TOOL IS FOR AUTHORIZED SECURITY TESTING ONLY!**

- ✅ Use responsibly
- ✅ Test legally
- ✅ Get permission
- ✅ Document everything
- ❌ Don't misuse
- ❌ Don't hack
- ❌ Don't invade privacy
- ❌ Don't break laws

**Remember: With great power comes great responsibility. Use ethically!**
