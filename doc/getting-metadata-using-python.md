Programmatically Getting the Metadata
=======================================

```{note}
The “metadata” or “instrument response files” complement the raw waveform data, providing the information that seismologists use for data processing, including:
  - gains, overall sensitivity, poles, zeros and filters needed to deconvolve the data and arrive at true ground motion
  - latitude, longitude, elevation (which are obfuscated to ~1 km to protect user’s identities)instrument type
  - any and all changes over time (since May, 2019)
```

To get individual instrument-response-file using python:

1. Make sure you have `python` installed. To check if you have python properly installed, run this command in the terminal:
  ```bash
  python --version
  ```
  or
  ```bash
  python3 --version
  ```
  ```{note}
  If python is not installed yet, please refer to their [official site](https://www.python.org/downloads/) to get the installer depending on your machine.
  ```
2. Install the necessary python packages:
  ```bash
  pip install obspy matplotlib
  ```
    
3. Save the python script below into a file named `get_inst_resp_file.py`.
  ```python
  from obspy.clients.fdsn import Client
  from obspy import UTCDateTime
  
  import matplotlib.pyplot as plt
  
  try:
    rs = Client('https://earthquake.science.upd.edu.ph')  # Specify the FDSN client here
    stn = 'RE722'  # Specify your station name here
    inv = rs.get_stations(network='AM', station=stn, level='RESP')

    fig = inv.plot_response(0.001, station=stn, show=False)

    # Save the instrument response plot into a PNG file
    fig.set_size_inches(12, 8)  # Set the output size
    fig.savefig(stn + "_inst_resp_file.png", dpi=300) 

    # Save the instrument response information into an XML file
    inv.write(stn + "_inst_resp_file.xml", format="STATIONXML")

    # Print a message indicating the successful retrieval and saving of the instrument response files
    success_message = f"Instrument response files for station '{stn}' have been successfully retrieved and saved:"
    print(f"\033[92m{success_message}\033[0m")
    print(f"- PNG plot: {stn}_inst_resp_plot.png")
    print(f"- XML metadata: {stn}_inst_resp_file.xml")
  
  except Exception as e:
    # Handle any exceptions that occur during execution
    error_message = f"An error occurred:"
    print(f"\033[91m{error_message}\033[0m")
    print(f"{e}")
  ```
  ```{note}
  To get the instrument response file of other station, just  change the value of the `stn` variable to your desired station name.
  ```
4. Run the python script in terminal using the command:
  ```bash
  python3 get_insp_resp_file.py
  ```
  After running the script, it will output a PNG file of the plot and an XML file of the instrument response information of the station specified in the script.
  

  ```{admonition} Sample Output
  ![Sample Output](_build/html/assets/_build/html/assets/getting-metadata-using-python/Sample_output.png)
  PNG and XML file outputs are saved on the same directory where you run the script.
  
  ![Sample instrument-response-file of RE722 station in PNG format.](_build/html/assets/getting-metadata-using-python/RE722_inst_resp_file.png)
  Sample instrument-response-file of RE722 station in PNG format.
  ```