Sending Data to EarthquakeHub Network
=======================================

For a citizen scientist to contribute their real-time Raspberry Shake data to the EarthquakeHub network, here are the steps to follow:


```{note}
Make sure that you have already <a href="https://upri-earthquake.github.io/installing-rshake-client.html" target="_blank"> installed the EarthquakeHub client on your Raspberry Shake device </a> before following this tutorial.
```



### 1. Register a `citizen` Account
   ![image](_build/html/assets/sending-data/3.1.png)


 To register an account go to
<a href="https://earthquake.science.upd.edu.ph" target="_blank">earthquake-hub web app</a> and click the `Sign Up` button. Choose `citizen` as your Role, and provide the following required details:
> - A valid email address
> - Account password



### 2. Device to Account Linking
   ![image](_build/html/assets/sending-data/3.2.png)


   In order for your device to stream data to the network, you should first link your device into your account.  This step will be done via the EarthquakeHub rShake client accessible via <a href="https://rs.local:3000" target="_blank">rs.local:3000.</a> To link your device, just click the `Link` button and input the account credentials you registered in Step 1, and the location information of your device:
   > - Elevation (in meters)
   > - Longitute (in degree coordinates)
   > - Latitude (in degree coordinate)

   You may use <a href="https://google.com/maps" target="_blank">Google Maps</a> to search your location on the map. Get the latitude and longitude coordinates by right clicking your pinned location on the map.
     ![image](_build/html/assets/sending-data/3.3.png)


### 3. Adding a Host
  ![image](_build/html/assets/sending-data/3.4.png)

   After having linked your device, you are now ready to send data to any available server on the network. This step will also be done via the <a href="https://rs.local:3000" target="_blank">EarthquakeHub rShake client.</a> To do this, click `Add Server` and choose your target ringserver from the dropdown list displayed.

