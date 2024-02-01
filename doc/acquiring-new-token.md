Acquiring New Token for your rShake Device
=====================
All rshake devices that is connected to the EarthquakeHub network will acquire tokens from the server to ensure security within the network. Each token expires every `99 days` from the date of acquiring one. Upon expiry of token, citizen scientist's device will not be able to stream properly to the server. To start streaming again, please follow the instructions on how to acquire new token: 
### 1. Unlink your device
   Navigate to `rs.local:3000` in your web browser and locate the “Unlink” button on the webpage. Follow the prompts to unlink your device. 
   ```{note}
   Make sure to note down your device location inputs such as longitude, latitude, and elevation. You will need these details for the re-linking process.
   ```
### 2. Link your device again
   Click the “Link” button on the webpage. Input the device location details (longitude, latitude, elevation) that you noted down earlier when prompted then submit.
### 3. Connect to a ringserver
   Once your device is successfully linked, proceed to add a new ringserver to start streaming to the server again.