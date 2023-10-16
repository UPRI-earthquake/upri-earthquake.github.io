How to Use FDSNWS to Download Ground Motion Data
===============================================

### Introduction
**FDSNWS** (Federation of Digital Seismograph Networks Web Services) is a set of web services that allow users to access and retrieve seismic data from various seismological networks and data centers. This documentation will guide you through the process of using FDSNWS to download ground motion data and its metadeta from the UPRI EarthquakeHub Network. Understanding the distinction among these two is essential to make interpretations more significant. In the context of FDSNWS,

**Data:** This is the actual seismic information you're interested in, like the earthquake measurements, shaking patterns, and seismograph readings.

**Metadata:** Metadata in FDSNWS provides important details about the data. It includes information such as when and where the seismic event occurred, how strong it was, and the equipment used to record the data. Think of metadata as helpful labels that give you context and understanding about the seismic data you're looking at.

### Service Overview

FDSNWS provides various services for accessing different types of data.
The most commonly used service for ground motion data is the ```dataselect```
service. While the ```event``` service is used to obtain the metadata

#### DataSelect
This service  allows you to retrieve time series data from seismological instruments. In the context of seismology, time series data refers to recordings of ground motion or seismic activity ***over time.***

Here are the following data you can gather from ```dataselect``` service

1. ***Seismic Waves:*** From the dataselect service, you can fetch actual data about the movement of the Earth's surface during events like earthquakes. Think of this as a detailed record of how the ground shakes during such events.

2. ***Time Charts:*** You can request time charts that show you how this shaking changes over time. These charts help scientists and researchers analyze and study the seismic activity.

3. ***Instrument Info:*** This service can also provide information about the tools (instruments) used to capture this seismic data. Understanding these instruments is crucial for correctly interpreting and using the data.


More information about DataSelect [here](https://www.fdsn.org/webservices/fdsnws-dataselect-1.1.pdf)

#### Event
This service is designed to provide access to information about seismic events.

Here are the following data you can gather from ```event``` service

1. ***Earthquake Information:*** The event service gives you details about specific seismic events, particularly earthquakes. This includes where they happened, how strong they were, and when they occurred.

2. ***Event Background:*** You can access additional information about the event's source, which helps in understanding what caused the event, whether it was a natural earthquake or something else.

3. ***Station Details:*** This service also offers information about the stations that recorded data for a specific event. This helps in verifying the data's reliability and its sources.

More information about Event [here](https://www.fdsn.org/webservices/fdsnws-event-1.2.pdf)


### Steps to Download Ground Motion Data

To obtain the Ground Motion Data, we will be using the "dataselect" service.


1. Access the [UPRI Earthquake Hub SeisComP FDSNWS Web Service](https://earthquake.science.upd.edu.ph/fdsnws/)
2. Choose the ```dataselect/``` web service
**<PHOTO HERE>**

3. Proceed by choosing ```1/```

4. Select builder from the options to proceed to the URL Builder where you will input your information request.

5. Specify the parameters of the data you want to download. This includes:
<time format>

**Network Code:** The abbreviation for the seismological network.
**Station Code:** The code for the specific seismic station.
**Location Code:** A two-character code specifying the location of the instrument at the station (usually "00" for the main channel).
**Channel Code:** The code for the specific channel of data (e.g., "BHZ" for a broadband horizontal component).
**Start Time:** The beginning time for the data you want. This cannot be the date at present or future.
**End Time:** The end time for the data you want.

> **_NOTE:_** The time is formatted **YYYY-MM-DDT-HH-MM-SS** The date and time is separated by the "T". The time is in 24-Hour (military time format).

> For example, we wanted to to obtain data starting from ``` October 11, 2023 at 11:30 pm till October 15, 2023 11:30 am``` start and end time should be ```2023-10-11T-23:30:00 and 2023-10-15T-11:30:00``` respectively.

**Data Format:** For Ground Motion, the data is in **miniseed** format

5. After filling out the form, click the link to start downloading data through clicking the URL located at the bottom part of the page.
**<PHOTO HERE>**







-dataselect
discuss the type of data

-event

-screenshots

2. Select Data Parameters
Specify the parameters of the data you want to download. This includes:
<time format>

**Network Code:** The abbreviation for the seismological network.
**Station Code:** The code for the specific seismic station.
**Location Code:** A two-character code specifying the location of the instrument at the station (usually "00" for the main channel).
**Channel Code:** The code for the specific channel of data (e.g., "BHZ" for a broadband horizontal component).
**Start Time:** The beginning time for the data you want.
**End Time:** The end time for the data you want.
**Data Format:** Choose the format you want the data in (MiniSEED).

3. Access the FDSNWS Query
Access the query URL written below the page **url sa fdsnws**

**url**

4. Use Software or Libraries
You can use various software tools or libraries to retrieve data using the constructed query URL. Commonly used options include: **obspy**

**url**

5. Save and Process the Data
Once you've downloaded the data, you can save it in your preferred format and process it as needed for your specific analysis or research.
-Plotting
-Print Information from the metadata (obspy)
do the same from following the documentation
