## Sending Data to EarthquakeHub Network:
For a citizen scientist to contribute their real-time Raspberry Shake data to the EarthquakeHub network here are the steps to follow:

> Note: Make sure that you have already [installed the EarthquakeHub client on your Raspberry Shake device](upri-earthquake.github.io/client-installation) before following this tutorial.

1. **Register a `citizen` Account:**
   > add screenshot here

   To register an account go to [earthquake-hub web app](https://earthquake.science.upd.edu.ph) and click the `Sign Up` button. Choose `citizen` as your Role, and provide the following required details:
     - A valid email address
     - Account password

1. **Adding a Device:**
   > add screenshot here
   
   After submitting the sign-up form, your Dashboard page shall appear.In order for your device to stream data to the network, you should first add a record of your device into your account. To do so, still in the [earthquake-hub web app](https://earthquake.science.upd.edu.ph), click the `Add Device` button on the Dashboard and provide the following details:
     - Network code
     - Station code
     - Elevation (in meters)
     - Longitute (in degree coordinates)
     - Latitude (in degree coordinate)

1. **Device to Account Linking:**
   > add screenshot here
   
   To ensure that the device record added on your account corresponds to an actual physical device, device linking must be performed. This step will be done via the EarthquakeHub rShake client accessible via [rs.local:3000](rs.local:3000). To link your device, just click the `Link` button and input the account credentials you registered in Step 1.  

1. **Adding a Host:**
   > add screenshot here
   
   After having linked your device, you are now ready to send data to any available server on the network. This step will also be done via the [EarthquakeHub rShake client](rs.local:3000). To do this, click `Add Server` and input the following details of the host you want to send your Raspberry Shake data to: 
     - Target ringserver's url
     - Hostname of the ringserver
   
