Updating the Rshake Client Software
=====================
Follow this guide to update the EarthquakeHub client software on an existing Raspberry Shake device.

## EarthquakeHub Raspberry Shake Device Update Guide

**Time needed:** 10-15 minutes

**Requirements:**

- Raspberry Shake device powered on and connected to the internet
- Laptop or desktop computer connected to the same network as the Raspberry Shake
- SSH access to the device

## Update an Existing Device

Use these steps for devices that already have the EarthquakeHub client installed and need the latest version.

### Step 1: Confirm that both devices are on the same network

Before starting, make sure your Raspberry Shake and your laptop or desktop computer are connected to the same network.

### Step 2: Connect to the Raspberry Shake

Open a terminal or command prompt, then connect to the device through SSH:

```bash
ssh myshake@rs.local
```

When prompted for the password, use your configured SSH password. If it was not changed, the default password is:

```bash
shakeme
```

### Step 3: Remove the old client software

After logging in successfully, run the uninstall script:

```bash
bash <(curl https://raw.githubusercontent.com/UPRI-earthquake/sender-backend/rshake-alerts/uninstall.sh)
```

### Step 4: Install the latest client software

When the uninstall script finishes, run the installation script:

```bash
bash <(curl https://raw.githubusercontent.com/UPRI-earthquake/sender-backend/rshake-alerts/install.sh)
```

### Step 5: Reboot the Raspberry Shake

After the installation completes, the installer will ask:

```bash
Reboot rshake device to apply the changes? (y/n):
```

Type **y**, then press **Enter**. Wait a few minutes for the device to restart.

> **Note (current default behavior):** The installer now uses `--reboot-policy always` by default, so it reboots automatically after install and may skip the manual reboot prompt. If your SSH session disconnects right after install, that is expected. Wait for the device to come back online, then continue to Step 6.

To keep a manual decision flow, run the install command with `--reboot-policy on-failure` or `--reboot-policy never`.

### Step 6: Check that the services are running

After the reboot, connect to the Raspberry Shake again:

```bash
ssh myshake@rs.local
```

Check the running containers:

```bash
docker ps -a
```

Confirm that the `sender-backend` and `sender-frontend` containers are running and are not in an exited state.

If either container is stopped, start it manually:

```bash
sender-backend START
sender-frontend START
```

### Step 7: Open the device web interface

In a web browser, open:

```bash
http://rs.local:3000
```

### Step 8: Link the device and add the server

<img width="2559" height="1407" alt="device-to-account-link" src="https://github.com/user-attachments/assets/c9cbfdff-c58a-4e3f-aed4-031e803be815" />

If the device is not linked to an EarthquakeHub account:

1. Click **Link**
2. Enter the EarthquakeHub account credentials previously used for this device
3. Fill in the required location details

If you forgot the account password, go to the EarthquakeHub web app at <https://earthquake.science.upd.edu.ph>, open the account button at the top-right, then use the forgot password option.

<img width="2559" height="1405" alt="adding-ringserver" src="https://github.com/user-attachments/assets/1b136f44-dd1b-4e17-88b8-38c4c662c299" />

After linking the device:

1. Click **Add Server**
2. Choose **UP-Diliman**
3. Confirm and wait for the stream to connect

## Troubleshooting: Device Stuck on "Connecting"

This section is only for edge cases where the device remains stuck on **Connecting** after the update.

<img width="480" height="360" alt="recovery-and-reset" src="https://github.com/user-attachments/assets/f68c2770-b948-46c6-b6b6-f4166afd2cf4" />

1. Open the **Status** tab (top-right)
2. If the status says **no refresh token saved**, go to **Recovery and Reset**
3. Reset the device link
4. Link the device again
5. Add the **UP-Diliman** server again
