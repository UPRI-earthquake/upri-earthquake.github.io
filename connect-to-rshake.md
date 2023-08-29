# How to Connect to Your Raspberry Shake via SSH

Connecting to your Raspberry Shake using SSH allows you to access and manage your device remotely. The following is a step by step guide to setup and connect to your Raspberry Shake from Windows (using either PuTTY or Powershell), from Mac, and from Ubuntu.

## Hardware Setup
   - Connect the power brick to your Raspberry Shake to power it on.
   - Connect one end of an ethernet cable to your Raspberry Shake and plug the other end into an ethernet port on the back of your router.

## How to SSH via Windows PuTTY
   - Open the PuTTY application.
   - Under Host Name (or IP address), enter your Raspberry Shake’s address, by default this is `rs.local`.
   - Make sure that Port is set to 22.
   - Under Connection type, select SSH.
   - Select Open, and enter Raspberry Shake username and password. By default, these are `myshake` and `shakeme`, respectively.

## How to SSH via Windows Powershell
   - To open PowerShell, either press Ctrl + Shift + P, or hit the Windows key and manually search for PowerShell.
   - Enter this SSH command: `ssh myshake@rs.local` which means to connect the user `myshake` to the device accessible via the address `rs.local` (which is your Raspberry Shake device in your local network).
   - You will be prompted to enter a password. The default password is `shakeme`. Usually, it wouldn't show any characters as you type, but simply type your password and press <ENTER> afterwards.

## How to SSH via Mac
   - Navigate to Applications > Utilities, and open the Terminal application.
   - Enter this SSH command: `ssh myshake@rs.local`
   - You will be prompted to enter a password. The default password is `shakeme`. Usually, it wouldn't show any characters as you type, but simply type your password and press <ENTER> afterwards. 


## How to SSH via Ubuntu
   - Press Ctrl + Alt + T to open a terminal.
   - Enter this SSH command: `ssh myshake@rs.local`
   - You will be prompted to enter a password. Type the default password `shakeme` and press <ENTER>.
     
___
**Note:** For improved security, it's highly recommended to change the default password of your Raspberry Shake. To learn how to update your password and access essential guidelines for securing your device effectively, refer to this [guide](https://manual.raspberryshake.org/hacked.html#hacked). 
