TV Bouquet File Creator
=======================

This Python script reads services/channels from an M3U file and generates a TV bouquet file in the desired format. The output bouquet file includes all the extracted services, and saves it with a user-defined name.

Features
--------

-   Reads channels/services from an M3U file.

-   Extracts the service identifiers from the provided URLs.

-   Generates a bouquet file with the desired name.

-   Simple and user-friendly.

Prerequisites
-------------

-   Python 3.x installed on your system.

How to Use
----------

1.  **Clone or download the repository:**

    ```
    git clone https://github.com/your-username/tv-bouquet-creator.git
    cd tv-bouquet-creator
    ```

2.  **Prepare your M3U file:** Ensure your M3U file is formatted correctly. Example format:

    ```
    #EXTM3U url-tvg="http://example.com/epg"
    #EXTINF:-1 tvg-id="ChannelID" tvg-name="ChannelName" tvg-logo="http://example.com/logo.png" group-title="GroupTitle",ChannelName
    http://10.0.0.227:8001/1:0:1:20B0:808:2:11A0000:0:0:0:
    ```

3.  **Run the script:**

    ```
    python create_bouquet.py
    ```

4.  **Provide the required inputs:**

    -   Enter the path to your M3U file when prompted.

    -   Enter a name for your bouquet file (e.g., `MyBouquet`).

5.  **Output:** The script will generate a bouquet file named `userbouquet.<YourBouquetName>.tv` in the script's directory. Example output format:

    ```
    #NAME MyBouquet
    #SERVICE 1:0:1:20B0:808:2:11A0000:0:0:0:
    ```

Example Usage
-------------

**Input:**

-   M3U file path: `channels.m3u`

-   Bouquet name: `MyBouquet`

**Generated File:** `userbouquet.MyBouquet.tv`

```
#NAME MyBouquet
#SERVICE 1:0:1:20B0:808:2:11A0000:0:0:0:
#SERVICE 1:0:19:2851:7FE:2:11A0000:0:0:0:
```

Error Handling
--------------

-   If the M3U file path is invalid, the script will prompt an error.

-   If no services are found in the M3U file, it will notify you.

Requirements
------------

-   A valid M3U file.

-   Python 3.x

<a href="https://www.buymeacoffee.com/CurtisFeatures" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
