UPRI EarthquakeHub Documentation Configuration
==================================

Welcome to the UPRI EarthquakeHub Documentation Configuration! This document will provide you with the necessary steps to access and navigate the project's documentation, including instructions for downloading dependencies required for Sphinx, our chosen documentation generator.


## Table of Contents

1. Introduction
2. Accessing the Documentation
3. File Directory
4. Deploying on GitHub Pages
5. Contributing
6. Feedback and Support


### 1. Introduction

The [UPRI EarthquakeHub](https://upri-earthquake.github.io/) contains all the information you need to understand and work with our project. We use Sphinx to generate and maintain this documentation, and the following sections will guide you through the process of accessing it.

### 2. Accessing the Documentation
To access the project documentation, follow these steps:

1. **Fork the Documentation Repository:** Forking a repository is creating a personal copy of a project you want to work on independently. Follow the steps to fork:

- Click on the [upri-earthquake.github.io](https://github.com/UPRI-earthquake/upri-earthquake.github.io) repository
- Click "Fork"
- Select the Destination: When you click "Fork," you'll be prompted to select where you want to fork the repository. Fork it to your user account

Congratulations! You are now have a copy of the project that is under your control, and you can make changes to it as you would with any other Git repository.


2. **Clone the Repository:** If you haven't already, clone the project's repository to your local machine using Git. You can do this by running the following command:

```
git clone https://github.com/your-project/repository.git
```

3. **Navigate to the Documentation Directory:** In this repository, the documentation files are stored in a folder named "doc".

```
cd repository/doc
````

4. **Open the Documentation:** Depending on the format, you can access the documentation using a web browser for HTML-based documentation, or a text editor for Markdown, RST or other text-based formats.

### 3. File Directory
The content of the documentation are written in different files. These files are deployed in the ```index.rst``` file. Should you wish to modify the content, follow the steps below:
1. Refer to the [Contributing Guide]() before making any changes.
2.  Identify which part of the documentation you want to edit. You may find these files in the ```doc``` folder. You may use any text editor to configure the files. Refer to the list of Markdown files and their corresponding topics:

**Tutorial**

- ```connect-to-rshake.md``` - How to Connect to Your Raspberry Shake via SSH
- ```installing-rshake-client.md``` - Installing EarthquakeHub Client on Raspberry Shake
- ```sending-data-to-ehub-network.md``` - Sending Data to EarthquakeHub Network
- ```fdsnws.md```How to Use FDSNWS to Download Ground Motion Data and Metadata
- ```intro-to-seiscomp.md``` - Introduction To SeisComp
- ```dev-guide-contributing.md``` - Developer Guide: Contributing
- ```docker-cheatsheet.md``` - Developer Guide: Docker Cheatsheet

**Documentation**

- ```system-overview.md``` - System Overview
- ```ehub-commons.md``` - earthquake-hub-commons
- ehub-backend/```overview.md``` -  earthquake-hub-backend
    **API Docs**
    - ehub-backend/api-docs/ ```ehub-backend-api-docs.json```


- sender-backend/```overview.md``` - sender-backend
    **API Docs**
    - sender-backend/api-docs/ ```sender-backend-api-docs.json```
- ```ringserver.md``` - RingServer
- ```skink2dali.md```- Slink2Dali

3. Save and Commit changes
Detailed instructions written [here](https://alyssapatricia.github.io/ui/dev-guide-contributing.html)


### 4. Deploying on GitHub Pages
To deploy your documentation on GitHub Pages, follow these steps:

1. Configure GitHub Pages: In your Forked GitHub repository, go to the "Settings" tab and scroll down to the "GitHub Pages" section. Set the source branch to "gh-pages" and the "root" folder. Save the changes.
2. Access the Published Documentation: After a few moments, your documentation will be available at the URL mentioned in the GitHub Pages settings, typically in the format: https://```<username>```.github.io/```<repository>```/.


### 5. Contributing
If you find any issues with the documentation or would like to contribute to its improvement, please refer to the [Contributing file](https://alyssapatricia.github.io/ui/dev-guide-contributing.html) in the repository.
It will provide guidance on how you can make updates or suggest improvements.


### 6. Feedback and Support
If you have any questions, encounter issues, or need support related to the project or its documentation, please reach out to our support team or open an issue on the project's repository.

Thank you for using our project documentation. We hope it serves as a valuable resource for your work. If you have any suggestions for improvements or additional information, please don't hesitate to contribute or provide feedback. We appreciate your involvement in making this documentation even better.

