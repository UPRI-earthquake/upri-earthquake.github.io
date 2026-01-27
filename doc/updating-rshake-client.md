Updating the Rshake Client Software
=====================
Follow the steps here to perform software update on your rshake device.
## Earthquake Hub Rshake Device Update Guide
**Time needed:** 10–15 minutes
**Requirements:**
- Device powered on and connected to the internet
- Phone, tablet, or computer on the same network

## UPDATE / FIX AN EXISTING DEVICE
*(For devices already installed but not working properly or stuck connecting)*
### Step 1: Connect to your device
```bash
ssh myshake@rs.local
```
_Use the default password if not changed._

---
### Step 2: Run the update
Copy, paste, then press **Enter**:
```bash
bash <(curl https://raw.githubusercontent.com/UPRI-earthquake/sender-backend/main/update.sh)
```

---
### Step 3: Reboot when asked
When prompted:

```bash
Reboot rshake device to apply the changes? (y/n):
```
Type **y**, then press **Enter**
Wait a few minutes for the device to restart.

---
### Step 4: Start the software
Connect again:

```bash
ssh myshake@rs.local
```
Then run:
```bash
sender-backend START
sender-frontend START
```

---
### Step 5: Open the device page
Go to:
```bash
http://rs.local:3000
```

---
### Step 6: Link and add server
<img width="2559" height="1407" alt="device-to-account-link" src="https://github.com/user-attachments/assets/c9cbfdff-c58a-4e3f-aed4-031e803be815" />

If the device is not linked:
1. Click **Link**
2. Enter your Earthquake Hub account credentials.
3. Fill in location details

<img width="2559" height="1405" alt="adding-ringserver" src="https://github.com/user-attachments/assets/1b136f44-dd1b-4e17-88b8-38c4c662c299" />

After linking:
1. Click **Add Server**
2. Choose **UP-Diliman**
3. Confirm and wait for the stream to connect


---
### Step 7: If stuck on “Connecting”
<img width="480" height="360" alt="recovery-and-reset" src="https://github.com/user-attachments/assets/f68c2770-b948-46c6-b6b6-f4166afd2cf4" />

1. Open the **Status** tab (top-right)
2. If it says **“no refresh token saved”**:
    - Go to **Recovery and Reset**
    - Reset device link
    - Link again
    - Add **UP-Diliman** server again
