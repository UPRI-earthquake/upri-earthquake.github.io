Introduction To SeisComp
========================

**SeisComp** is a seismological software that has been developed collaboratively by the GEOFON Program at Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences and gempa GmbH. It plays a vital role in various aspects of seismological operations, encompassing data acquisition, processing, distribution, and interactive analysis.

While SeisComP is employed by the EarthquakeHub Network for processing seismic data sourced through citizen science efforts, it's important to note that its use is not an absolute requirement within the EarthquakeHub Network. Alternative data processing software capable of handling miniseed data can also be employed for processing network data.

SeisComP encompasses a suite of modular components, each dedicated to specific tasks, including:
1. **Global Parameters:** Unified schema for configuring each modules.
2. **Acquisition:** Responsible for data collection.
3. **Inventory:** Manages network information.
4. **Messaging:** Facilitates communication between system elements.
5. **Processing:** Executes advanced data analysis and interpretation.
6. **Utilities:** Offers various auxiliary tools for enhanced functionality.


## Installation from Pre-Compiled Release Package
This guide provides instructions for installing SeisComP packages on machines running Ubuntu. These guide works for Ubuntu 20.04 and 22.04, as of this writing. For more comprehensive installation details, please consult the <a href="https://www.seiscomp.de/doc/base/installation.html" target="_blank">official documentation.</a>


1. Begin by creating a directory where you intend to download and install SeisComP packages.
2. Navigate to the directory you've just created and download the appropriate SeisComP binary package compatible with your Linux distribution and architecture. You can obtain this package from the <a href="https://www.seiscomp.de/downloader/" target="_blank">SeisComP download site</a>.

3. Within the same directory, retrieve the SeisComP maps using the following command:
    ```bash
    wget "https://www.seiscomp.de/downloader/seiscomp-maps.tar.gz"
    ```
4. Unpack the `seiscomp*` files, which include the binary package, maps, and documentation:
    ```bash
    tar xzf seiscomp-4.0.0-ubuntu20.04-x86_64.tar.gz
    ```
    ```bash
    tar xzf seiscomp-maps.tar.gz
    ```
    ```bash
    tar xzf seiscomp-4.0.0-doc.tar.gz
    ```


```{note}
For some packages, documentations are already included in the downloaded seiscomp package so there is no need to download and unpack the documentation.
```

You may check that all files are properly unpacked by running the `ls` command:
```
ls seiscomp
bin  etc  include  lib  man  sbin  share
```
5. Execute the following commands to install dependencies and set up the environment:
```bash
/seiscomp/bin/seiscomp install-deps base
```

```{note}
Depending on your Ubuntu version, additional steps may be required to address specific dependencies:```

- On Ubuntu 18: Install Python and related libraries:
```bash
sudo apt-get install python libqtgui4
```

- On Ubuntu 20 and newer: Ensure libpython3-dev is installed:
```bash
sudo apt-get install libpython3-dev
```

- Alternatively, for Mint 18 (Ubuntu 16.04):
```bash
      sudo apt-get update
      sudo apt-get install libxml2 libboost-filesystem1.58.0 libboost-iostreams1.58.0 libboost-thread1.58.0 libboost-program-options1.58.0 libboost-regex1.58.0 libboost-signals1.58.0 libboost-system1.58.0 libssl1.0.0 libncurses5 libmysqlclient20 libpq5 libpython2.7 python-numpy mysql-server mysql-client libqtgui4 libqt4-xml libqt4-opengl libqt4-sql-sqlite
```


6. Configure the database. You may choose to use either MariaDB or a MySQL for the database.

- For a MariaDB installation:

```bash
./seiscomp/bin/seiscomp install-deps mariadb-server
```

![image](_build/html/assets/intro-to-seiscomp/5.1.png)

- For a MySQL installation:
```bash
./seiscomp/bin/seiscomp install-deps mysql-server
    ```

## Getting Started
After installing seiscomp packages and configuring database, the next step is to setup seiscomp using `seiscomp setup` or the wizard from within scconfig.
1. Execute setup via:
```{note}
In seiscomp setup default values are given in brackets [ ]:
```

```bash
    seiscomp/bin/seiscomp setup

    ====================================================================
    seiscomp setup
    ====================================================================

    This initializes the configuration of your installation.
    If you already made adjustments to the configuration files
    be warned that this setup will overwrite existing parameters
    with default values. This is not a configurator for all
    options of your setup but helps to setup initial standard values.

    --------------------------------------------------------------------
    Hint: Entered values starting with a dot (.) are handled
          as commands. Available commands are:

          quit: Quit setup without modification to your configuration.
          back: Go back to the previous parameter.
          help: Show help about the current parameter (if available).

          If you need to enter a value with a leading dot, escape it
          with backslash, e.g. "\.value".
    --------------------------------------------------------------------
```



This will ask for initial settings. You may just leave the default values for the following details:

```bash
    Organization name []:
```

```
    Enable database storage [yes]:
    0) mysql
      MySQL server.
    1) postgresql
        PostgreSQL server. There is currently no support in setup to create the
        database for you. You have to setup the database and user accounts on
        your own. The database schema is installed under share/db/postgresql.sql.
    Database backend [0]:
    Create database [yes]:
```


For database root password, you may enter your desired password
```bash
MYSQL root password (input not echoed) []:
```
```
Drop existing database [no]:
Database name [seiscomp]:
Database hostname [localhost]:
```
Specify the desired user and password for both read-write and read-only access parameters.

```bash
Database read-write user [sysop]:
Database read-write password [sysop]:
Database public hostname [localhost]:
Database read-only user [sysop]:
Database read-only password [sysop]:
```


2. After addressing all questions, you'll need to make a final decision: proceed to create the initial configuration, return to the previous question, or exit without making any changes. Press <ENTER> to save the initial setup.

```bash
Finished setup
--------------

P) Proceed to apply configuration
B) Back to last parameter
Q) Quit without changes
Command? [P]:
```

## Adding New Station
In order to process seismic data within SeisComP, it's essential to define a data source, which is typically represented by a station. Follow these steps to add a new station to your SeisComP setup:
1. You will need `inventory` of the new station to be added. This information is typically stored in `.yml` format. To acquire the inventory, you can refer to the guide on [how to fetch inventory using FDSNWS]().
2. Once you have acquired the inventory data, the next step is to import it into SeisComP. Navigate to the terminal where SeisComP is installed and execute the following command:

```bash
./seiscomp/bin/seiscomp exec import_inv fdsnxml ./inventory_CLL.xml
```

The following output should be shown:

```bash
    Generating output to /home/user/seiscomp/etc/inventory/inventory_CLL.xml
    No inventory read from inventory db
    Create empty one
    Processing /home/user/inventory_CLL.xml
     - parsing StationXML
     - converting into SeisComP-XML
    Finished processing
    Writing inventory to /home/user/seiscomp/etc/inventory/inventory_CLL.xml
```

3. After successfully importing the inventory, update the SeisComP configuration by running:

```bash
    seiscomp update-config
```

## Getting Real-time Data from a Remote Seedlink Server
<a href="https://www.seiscomp.de/doc/base/tutorials/waveforms.html" target="_blank"> Refer to this link </a>

## Important concepts to know about seiscomp
- <a href="https://www.seiscomp.de/doc/base/concepts.html#concepts" target="_blank">Reference to SeisComp</a>
- Messaging: Exchanging information in real-time processing
- Database: Storing meta data, configurations and data products
- Modules: Daemon programs and command-line tools
- Inventory: Station meta data
- Configuration: Inventory, module and binding configurations




