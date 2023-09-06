## Sending Data to EarthquakeHub Network:
For a citizen scientist to contribute their real-time Raspberry Shake data to the EarthquakeHub network here are the steps to follow:

> Note: Make sure that you have already [installed the EarthquakeHub client on your Raspberry Shake device](upri-earthquake.github.io/client-installation) before following this tutorial.

1. **Register a `citizen` Account:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/8d63d412-422a-481f-811b-66adadd86723)


   To register an account go to [earthquake-hub web app](https://earthquake.science.upd.edu.ph) and click the `Sign Up` button. Choose `citizen` as your Role, and provide the following required details:
     - A valid email address
     - Account password

1. **Adding a Device:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/4194cf1e-a808-4b5b-8548-fda84b6c7b4a)

   After submitting the sign-up form, your Dashboard page shall appear.In order for your device to stream data to the network, you should first add a record of your device into your account. To do so, still in the [earthquake-hub web app](https://earthquake.science.upd.edu.ph), click the `Add Device` button on the Dashboard and provide the following details:
   > Note: You  may acquire the `Network Code` and `Station Code` by going to [http://rs.local](http://rs.local). The first two (2) letters is the Network Code. The next five (5) characters is your device's Station Code. In this example, the network code is _AM_ and the station code is _RE722_.
   > 
   > ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/a18a873b-252a-4d84-9b0d-abf5def51da5)
   > 
     - Network code
     - Station code
     - Elevation (in meters)
     - Longitute (in degree coordinates)
     - Latitude (in degree coordinate)

1. **Device to Account Linking:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/5905a34b-f8dd-4eb0-b231-6a4c7372764a)

   
   To ensure that the device record added on your account corresponds to an actual physical device, device linking must be performed. This step will be done via the EarthquakeHub rShake client accessible via [rs.local:3000](rs.local:3000). To link your device, just click the `Link` button and input the account credentials you registered in Step 1.  

1. **Adding a Host:**
   ![image](https://github.com/UPRI-earthquake/upri-earthquake.github.io/assets/80037186/2da5092e-f397-4319-b558-c9a295c53ad0)

   After having linked your device, you are now ready to send data to any available server on the network. This step will also be done via the [EarthquakeHub rShake client](rs.local:3000). To do this, click `Add Server` and choose your target ringserver  input the following details of the host you want to send your Raspberry Shake data to: 
     - Target ringserver's url
     - Hostname of the ringserver
   
