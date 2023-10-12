How to use FDSNWS to download ground motion data
------------------------------------------------------------

### What is FDSNWS?

**FDSNWS** is a server that provides event and station information by FDSN Web Services from a SeisComP database and waveforms from a [RecordStream](https://www.seiscomp.de/doc/apps/global_recordstream.html#global-recordstream) source. Also it may be configured to serve data availability information.

### Service Overview

The following services are available:

| Service | Provides | Provided format |
| --- | --- | --- |
| fdsnws-dataselect | time series data | miniSEED |
| fdsnws-station | network, station, channel, response metadata | FDSN Station XML, StationXML, SCML |
| fdsnws-event | earthquake origin and magnitude estimates | QuakeML, SCML |
| ext-availability | waveform data availability information | text, geocsv, json, sync, request (fdsnws-dataselect) |



### **DataSelect**


**Purpose:**

To specify a web service interfaces for the exchange of time series data within the context of the International Federation of Digital Seismograph Networks (FDSN). The intention is to provide a specification that, when implemented at different FDSN data centers, can be used interchangeably by the same client software.

- Provides time series data in miniSEED format
- Request type: HTTP-GET, HTTP-POST


**Service Methods:**
The service should support these methods:

- **query** – to submit a data request
- **queryauth** – to authenticate and submit a data request
- **version** – to request the full service version number
- **application.wadl** – to request a WADL for the interface


*Additional information for DataSelect [here](https://www.fdsn.org/webservices/fdsnws-dataselect-1.1.pdf)*


### Station

**Purpose:**

To specify a web service interface for the exchange of time series metadata within the context of the International Federation of Digital Seismograph Networks (FDSN). The intention is to provide a specification that, when implemented at different FDSN data centers, can be used interchangeably by the same client software.

- Provides network, station, channel, response metadata
- Request type: HTTP-GET, HTTP-POST
- Stations may be filtered e.g. by geographic region and time, also the information depth level is selectable
- Optionally handles time-based conditional HTTP-GET requests as specified by [RFC 7232](https://tools.ietf.org/html/rfc7232).

**Service methods:**

The service should support these methods:

- **query** – to submit a data or information request
- **version** – to request the full service version
- **application.wadl** – to request a WADL for the interface

[Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5f764407-9aec-438e-a113-422d896cf709/06b7a3b3-ce2a-496d-bc4c-852b7c193c9e/Untitled.png)

[Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5f764407-9aec-438e-a113-422d896cf709/7bafc4f9-a8ad-40b4-a772-a72838dd5ffb/Untitled.png)

### Event

**Purpose:**

To specify a web service interface for the exchange of event parameter and related data within the context of the International Federation of Digital Seismograph Networks (FDSN). The intention is to
provide a specification that, when implemented at different FDSN data centers, can be used interchangeably by the same client software.

- Provides earthquake origin and magnitude estimates
- Request type: HTTP-GET
- Events may be filtered e.g. by hypocenter, time and magnitude


**Service methods:**

The service should support these methods:
- **query** – to submit a data request
- **catalogs** – to submit a request for available catalogs
- **contributors** – to submit a request for available contributors
- **version** – to request the full service version number
- **application.wadl** – to request a WADL for the interface

### Data Availability

The data availability web service returns detailed time span information of what time series data is available at the DMC archive. The availability information can be created by [scardac](https://www.seiscomp.de/doc/apps/scardac.html#scardac) in the SeisComP database from where it is fetched by fdsnws.

The availability service is no official standard yet. This implementation aims to be compatible with the IRIS DMC availability FDSN Web Service (*IRIS DMC* [[12](https://www.seiscomp.de/doc/base/references.html#id135)]) implementation.

**Purpose:**

To specify a web service interface for the exchange of time series data availability within the context of the International Federation of Digital Seismograph Networks (FDSN). The intention is to provide a specification that, when implemented at different FDSN data centers, can be used interchangeably by the same client software.

- request type: HTTP-GET, HTTP-POST
- results may be filtered e.g. by channel code, time and quality


**Service Methods:**

The following methods shall be supported by the service:

- **query** – to submit a data request
- **queryauth** – to authenticate and submit a request, optional
- **extent** - to submit a data request
- **extentauth** – to authenticate and submit a request, optional
- **version** – to request the full service version number
- **application.wadl** – to request a WADL for the interface

-------------------------------------------------------

### How to Use FDSNWS (of our server) to Download Ground Motion Data and Station Metadata?

### Downloading miniseed data:

1. Go to https://earthquake.science.upd.edu.ph/fdsnws/ and select the `dataselect/` web service.
2. Proceed by choosing `1/`
3. Select `builder` from the options to proceed to the URL Builder where you will input your information request.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5f764407-9aec-438e-a113-422d896cf709/510ae7d3-7866-4462-b9fa-9b4ec5e5174e/Untitled.png)

1. After filling out the form, click the link to start downloading data.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5f764407-9aec-438e-a113-422d896cf709/fffce1fe-f2c0-46bb-a4b6-92c31689fcf4/Untitled.png)

### Downloading Station Metadata:
