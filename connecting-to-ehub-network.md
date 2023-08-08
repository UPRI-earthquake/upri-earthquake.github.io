## Connecting to EarthquakeHub Network:
EarthquakeHub Network is a citizen science network of ground motion sensors (such as, but not limited to, raspberryshakes) which enables data transmission, archiving, and allows feeding the network data to earthquake detection software (such as, but not limited to, SeisComP). For a citizen scientist to contribute data to the network here are the steps to follow:

1. **Register a `citizen` Account:**  
   To register for an account go to [earthquake-hub web app](https://earthquake.science.upd.edu.ph) and click the `Sign Up` button. Provide the following required details then submit the form:
     - A valid email address
     - Account password
2. **Adding a Device:**  
   Devices must be registered to an account first before it can stream data to the network. To do so, still in the [earthquake-hub web app](https://earthquake.science.upd.edu.ph), you must add your device via the `Add Device` button in your registered account's dashboard. Provide the following required details then submit the form:
     - Network code
     - Station code
     - Elevation (in meters)
     - Longitute (in degree coordinates)
     - Latitude (in degree coordinate)
3. **Device to Account Linking:**  
   Linking your physical device to your registered account in the network is a necessary step to ensure integrity of data collected in the network. This step will be done via the `sender web app` accessible through your local area network via [rs.local:3000](rs.local:3000). To link your device, just click the `Link` button and input the account name and password you registered in the earthquake-hub web app.  
4. **Adding a Host:**  
   This step will also be done via the [sender web app](rs.local:3000). To do this, click the `Add Server` button. Input the following details, then click submit button: 
     - Target ringserver's url
     - Hostname of the ringserver
   
