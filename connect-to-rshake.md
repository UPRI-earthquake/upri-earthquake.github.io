## How to Connect to Your Raspberry Shake via SSH

Connecting to your Raspberry Shake using SSH allows you to access and manage your device remotely. Follow these steps to establish an SSH connection:

1. **Network Setup:**
   - Connect one end of an ethernet cable to your Raspberry Shake.
   - Plug the other end into a port on the back of your router.

2. **Power On:**
   - Plug in the Raspberry Shake and power it on.

3. **SSH Connection:**
   - Open a terminal on your local computer. Make sure that your local computer and the device are on the same network.
   - Use the SSH command to connect to the Raspberry Shake. The default SSH port is 22.
     ```bash
     ssh myshake@rs.local
     ```
   - You will be prompted to enter a password. Type the default password (shakeme) and press <ENTER>.
     > **Note:** For improved security, it's highly recommended to change the default password. To learn how to update your password and access essential guidelines for securing your device effectively, refer to this [guide](https://manual.raspberryshake.org/hacked.html#hacked). 
   - If you're a Windows user, you can use [PuTTY](https://www.putty.org/) for this step.
