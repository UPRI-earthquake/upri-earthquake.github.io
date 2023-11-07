sender-backend
==========================

## Overview

RaspberryShake (rShake) devices are microcomputers which will be used by the earthquake-hub network to collect seismic data. This data will then be transmitted to one or more ringservers. The `sender-backend` is the main program executed to perform the task of data forwarding and other tasks related to it. This program will run within a docker container inside the rShake.

There are two main tasks performed by the sender-backend:

1. **Configuration & Monitoring via Web Application**
  Before an rshake can send data to a ringserver it is necessary to (1) link the physical device to a registered account for the citizen science network, and (2) to input the address of the destination ringserver.
  Given a connection you want to monitor, the program provides information regarding the streaming status to the ringserver hosts specified.
  These tasks are done via the webapp (frontend) that is served through the sender-backend.
>
2. **Spawning Slink2dali**
  `Slink2dali` is integrated to the sender-backend container, which is responsible for forwarding data from the rShake's seedlink server to remote ringservers. The backend application spawns the Slink2dali process, allowing it to retrieve locally available data from the rShake device and forward it to configured remote servers, like the UP Ringserver.



## API
This is the link for the <a href="https://upri-earthquake.github.io/sender-backend/api-docs/" target="_blank">API Docs</a>

## CONTRIBUTING.md
This is the link for <a href="https://github.com/UPRI-earthquake/sender-backend/blob/main/CONTRIBUTING.md" target="_blank">CONTRIBUTING.md</a>
