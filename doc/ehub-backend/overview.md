earthquake-hub-backend
==========================

## Overview

EarthquakeHub network is comprised of `rshake devices` that are used for transmission of real-time sensor data and `a central server` which processes and serves the received data for various purposes, including data archiving, earthquake detection, and public showcasing through the web application. `earthquake-hub-backend` is the server-side component of that web application. This is run within a docker container inside a dedicated server.

There are two main tasks performed by the earthquake-hub-backend:

1. **Authentication**
  By allowing only registered and authorized citizen scientists to contribute data to the network, we are ensuring the authenticity and integrity of the data within the EarthquakeHub network. This is done by integrating an authentication mechanism, as API, to the system; using JSON web tokens. These tokens will be used to determine the authenticity of clients who are requesting certain information to the server. Another use of these tokens is to identify whether a requesting client is permitted to write to the ringserver or not.
>

2. **Storage of Account Details, Device Information and Seismic Data**
  As a central server, earthquake-hub-backend houses the shared data of the whole network. Information regarding the account of those who registered in the network, device information such as location and name, and seismic-event information are all saved in the database.

## API

This is the link for the <a href="https://upri-earthquake.github.io/ehub-backend/api-docs/" target="_blank">API Docs</a>


## CONTRIBUTING.md
This is the link for <a href="https://github.com/UPRI-earthquake/earthquake-hub-backend/blob/main/CONTRIBUTING.md" target="_blank">CONTRIBUTING.md</a>

