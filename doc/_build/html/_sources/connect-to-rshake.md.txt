How to Connect to Your Raspberry Shake via SSH
================================================


Connecting to your Raspberry Shake using SSH allows you to access and manage your device remotely. The following is a step by step guide to setup and connect to your Raspberry Shake from **Windows (using either PuTTY or Powershell)**, from **Mac**, and from **Ubuntu**.

## Hardware Setup
   - Connect the power brick to your Raspberry Shake to power it on.
   - Connect one end of an ethernet cable to your Raspberry Shake and plug the other end into an ethernet port on the back of your router.
   - Wait for the [Raspberry Shake's ethernet LED indicators](https://manual.raspberryshake.org/specifications.html#led-behavior) to behave as follows:
       - Green light (flashing repeatedly)
       - Orange light (solid)

     **This means that the ethernet port is working as it should.**

## How to SSH via Windows Powershell
   - To open PowerShell, either press Ctrl + Shift + P, or hit the Windows key and manually search for PowerShell.
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/83d6967d-1881-4531-89d0-4454865feb3f)

-----

   - Enter this SSH command: `ssh myshake@rs.local` which means to connect the user `myshake` to the device accessible via the address `rs.local` (which is your Raspberry Shake device in your local network). If it asks to validate the authenticity of the host, simply type "yes"
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/f77266ea-514a-4186-9660-bbe5733bacc9)

-----

   - You will be prompted to enter a password. The default password is `shakeme`. Usually, it wouldn't show any characters as you type, but simply type your password and press ENTER afterwards.
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/7ad5d336-7a5a-4e24-bf79-dcb2c4dcd6d6)

-----

   - Once successfully connected, the terminal you are in is now controlling the system of your Raspberry Shake device. You may try the `myshake` command to get a status log of your device. In this case, my test device has a network-station code of `AM_RE722`, this should be different from the code of your device.
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/d361ed0a-cbd6-4ddd-8660-bd69fda7c96c)

-----

   - After you have completed your purpose for connecting to the device, you may close the SSH connection by simply typing `exit` to the prompt. This would return you to the normal terminal prompt for your PC.
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/b2f6693c-bd00-4bad-ae6d-8c8764ee1681)


## How to SSH via Windows PuTTY
   - To open the PuTTY application, press the Windows key and search for "putty".
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/086ff76f-ce96-4c80-8c8b-e3191d84e35d)

     > If PuTTY is not yet installed, you may follow [this link to get the application via Microsoft Store.](https://apps.microsoft.com/store/detail/putty/XPFNZKSKLBP7RJ) Or if you prefer not to download anything, you may try connecting via Powershell instead which comes pre-installed in most Windows operating systems.

------
   - Input the following:

     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/2c18f9c4-ad07-44b2-ad94-78034c5bd5a6)
       - Under Host Name (or IP address), enter your Raspberry Shake’s address, by default this is `rs.local`.
       - Make sure that Port is set to 22.
       - Under Connection type, select SSH.

-----

   - Click Open, and enter Raspberry Shake username and password. By default, these are `myshake` and `shakeme`, respectively. If it asks about trusting the host, simply click Accept.

     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/3fa1adbc-11d0-48c1-afd5-18377b17fa7b)

-----

   -  Once successfully connected, the terminal you are in is now controlling the system of your Raspberry Shake device. You may try the `myshake` command to get a status log of your device. In this case, my test device has a network-station code of `AM_RE722`, this should be different from the code of your device.
     ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/9a878ba2-2657-4c25-9ecc-31d56b670965)

-----

   - After you have completed your purpose for connecting to the device, you may close the SSH connection by simply typing `exit` to the prompt. This should exit the terminal window and you are effectively disconnected from the device.

## How to SSH via Mac
   - Navigate to Applications > Utilities (or Other), and open the Terminal application. You may also pres Cmd+Space and type "Terminal"
   <img width="1440" alt="Screen Shot 2023-08-29 at 3 04 26 PM" src="https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/ad82216a-7f83-46e2-b58f-148b24606182">

-----

   - Enter this SSH command: `ssh myshake@rs.local`
     <img width="793" alt="Screen Shot 2023-08-29 at 3 10 25 PM" src="https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/3a32a500-c33f-4123-8dfb-f01231cd7aba">

-----

   - You will be prompted to enter a password. The default password is `shakeme`. Usually, it wouldn't show any characters as you type, but simply type your password and press <ENTER> afterwards.
     <img width="794" alt="Screen Shot 2023-08-29 at 3 11 09 PM" src="https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/62192209-f7f9-421f-b16e-f4069d7b155b">

-----

   - Once successfully connected, the terminal you are in is now controlling the system of your Raspberry Shake device. You may try the `myshake` command to get a status log of your device. In this case, my test device has a network-station code of `AM_RE722`, this should be different from the code of your device.
     <img width="795" alt="Screen Shot 2023-08-29 at 3 12 43 PM" src="https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/16431c3b-ddba-48f6-bfa9-3b12ba2cb45a">

-----

   - After you have completed your purpose for connecting to the device, you may close the SSH connection by simply typing `exit` to the prompt. This would return you to the normal terminal prompt for your macOS.
     <img width="795" alt="Screen Shot 2023-08-29 at 3 13 25 PM" src="https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/47804913/89a555a1-df80-4479-b599-6c6590218a3b">




## How to SSH via Ubuntu
   - Press Ctrl + Alt + T to open a terminal.
   - Enter this SSH command: `ssh myshake@rs.local`
   - You will be prompted to enter a password. Type the default password `shakeme` and press <ENTER>.

___

> **_NOTE:_**  For improved security, it's highly recommended to change the default password of your Raspberry Shake. To learn how to update your password and access essential guidelines for securing your device effectively, refer to this [guide](https://manual.raspberryshake.org/hacked.html#hacked).

