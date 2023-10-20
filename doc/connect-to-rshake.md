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
     ![image](_build/html/assets/connecting-rshake/1.1.jpg)


   - Enter this SSH command: `ssh myshake@rs.local` which means to connect the user `myshake` to the device accessible via the address `rs.local` (which is your Raspberry Shake device in your local network). If it asks to validate the authenticity of the host, simply type "yes"
     ![image](_build/html/assets/connecting-rshake/1.2.jpg)

   - You will be prompted to enter a password. The default password is `shakeme`. Usually, it wouldn't show any characters as you type, but simply type your password and press ENTER afterwards.
     ![image](_build/html/assets/connecting-rshake/1.3.jpg)



   - Once successfully connected, the terminal you are in is now controlling the system of your Raspberry Shake device. You may try the `myshake` command to get a status log of your device. In this case, my test device has a network-station code of `AM_RE722`, this should be different from the code of your device.
     ![image](_build/html/assets/connecting-rshake/1.4.jpg)

-----

   - After you have completed your purpose for connecting to the device, you may close the SSH connection by simply typing `exit` to the prompt. This would return you to the normal terminal prompt for your PC.
     ![image](_build/html/assets/connecting-rshake/1.5.jpg)


## How to SSH via Windows PuTTY
   - To open the PuTTY application, press the Windows key and search for "putty".
     ![image](_build/html/assets/connecting-rshake/1.6.jpg)

     > If PuTTY is not yet installed, you may follow [this link to get the application via Microsoft Store.](https://apps.microsoft.com/store/detail/putty/XPFNZKSKLBP7RJ) Or if you prefer not to download anything, you may try connecting via Powershell instead which comes pre-installed in most Windows operating systems.

------
   - Input the following:

     ![image](_build/html/assets/connecting-rshake/1.7.jpg)

       - Under Host Name (or IP address), enter your Raspberry Shake’s address, by default this is `rs.local`.
       - Make sure that Port is set to 22.
       - Under Connection type, select SSH.

-----

   - Click Open, and enter Raspberry Shake username and password. By default, these are `myshake` and `shakeme`, respectively. If it asks about trusting the host, simply click Accept.

     ![image](_build/html/assets/connecting-rshake/1.8.jpg)

-----

   -  Once successfully connected, the terminal you are in is now controlling the system of your Raspberry Shake device. You may try the `myshake` command to get a status log of your device. In this case, my test device has a network-station code of `AM_RE722`, this should be different from the code of your device.
     ![image](_build/html/assets/connecting-rshake/1.9.jpg)

-----

   - After you have completed your purpose for connecting to the device, you may close the SSH connection by simply typing `exit` to the prompt. This should exit the terminal window and you are effectively disconnected from the device.

## How to SSH via Mac
   - Navigate to Applications > Utilities (or Other), and open the Terminal application. You may also pres Cmd+Space and type "Terminal"
   ![image](_build/html/assets/connecting-rshake/1.10.jpg)

-----

   - Enter this SSH command: `ssh myshake@rs.local`
     ![image](_build/html/assets/connecting-rshake/1.11.jpg)

-----

   - You will be prompted to enter a password. The default password is `shakeme`. Usually, it wouldn't show any characters as you type, but simply type your password and press <ENTER> afterwards.
     ![image](_build/html/assets/connecting-rshake/1.12.jpg)

-----

   - Once successfully connected, the terminal you are in is now controlling the system of your Raspberry Shake device. You may try the `myshake` command to get a status log of your device. In this case, my test device has a network-station code of `AM_RE722`, this should be different from the code of your device.
     ![image](_build/html/assets/connecting-rshake/1.13.jpg)

-----

   - After you have completed your purpose for connecting to the device, you may close the SSH connection by simply typing `exit` to the prompt. This would return you to the normal terminal prompt for your macOS.
     ![image](_build/html/assets/connecting-rshake/1.14.jpg)




## How to SSH via Ubuntu
   - Press Ctrl + Alt + T to open a terminal.
   - Enter this SSH command: `ssh myshake@rs.local`
   - You will be prompted to enter a password. Type the default password `shakeme` and press <ENTER>.

___

> **_NOTE:_**  For improved security, it's highly recommended to change the default password of your Raspberry Shake. To learn how to update your password and access essential guidelines for securing your device effectively, refer to this [guide](https://manual.raspberryshake.org/hacked.html#hacked).

