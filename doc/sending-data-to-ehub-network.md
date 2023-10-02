## Sending Data to EarthquakeHub Network:
For a citizen scientist to contribute their real-time Raspberry Shake data to the EarthquakeHub network here are the steps to follow:

> Note: Make sure that you have already [installed the EarthquakeHub client on your Raspberry Shake device](upri-earthquake.github.io/client-installation) before following this tutorial.

1. **Register a `citizen` Account:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/8d63d412-422a-481f-811b-66adadd86723)


   To register an account go to [earthquake-hub web app](https://earthquake.science.upd.edu.ph) and click the `Sign Up` button. Choose `citizen` as your Role, and provide the following required details:
     - A valid email address
     - Account password

1. **Device to Account Linking:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/335d9ec4-cf26-497f-8d82-c2dde262fba2)


   In order for your device to stream data to the network, you should first link your device into your account.  This step will be done via the EarthquakeHub rShake client accessible via [rs.local:3000](rs.local:3000). To link your device, just click the `Link` button and input the account credentials you registered in Step 1, and the location information of your device:

     - Elevation (in meters)
     - Longitute (in degree coordinates)
     - Latitude (in degree coordinate)

     > You may use [Google Maps](https://google.com/maps) to search your location on the map. Get the latitude and longitude coordinates by right clicking your pinned location on the map. ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/4ed9f828-5325-43d1-8b7a-b590ffc13231)



1. **Adding a Host:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/2da5092e-f397-4319-b558-c9a295c53ad0)

   After having linked your device, you are now ready to send data to any available server on the network. This step will also be done via the [EarthquakeHub rShake client](rs.local:3000). To do this, click `Add Server` and choose your target ringserver  input the following details of the host you want to send your Raspberry Shake data to:
     - Target ringserver's url
     - Hostname of the ringserver

