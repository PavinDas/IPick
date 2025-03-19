# IPick

A Python-based IP location tracker that peeks into the whereabouts of any IP address with a colorful twist!

<img src="https://socialify.git.ci/PavinDas/IPick/image?description=1&font=KoHo&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="Socket" width="640" height="320" />


---

## Overview

A lightweight Python script that fetches geolocation data for a given IP address. It displays details like city, ISP, country, and coordinates in a vibrant, colorized console output.

**Creator**: Pavin Das  
**GitHub**: [PavinDas](https://github.com/PavinDas)  
**Instagram**: [pavin__das](https://www.instagram.com/pavin__das)

---

## Features

- **IP Geolocation**: Retrieves city, ISP, country, region, timezone, ZIP, latitude, and longitude for any IP.
- **Colorful Output**: Uses `colorama` for a visually appealing console experience.
- **Simple Interface**: Just enter an IP address and get the details.
- **Error Handling**: Gracefully handles invalid IPs and user interrupts (`Ctrl+C`).
- **Lightweight**: Minimal dependencies and straightforward code.

---

## Requirements

- **Operating System**: Any (Windows, Linux, macOS)
- **Python**: 3.x
- **Dependencies**:
  - `requests` (for API calls)
  - `colorama` (for colored output)
- **Internet**: Required to query the `ip-api.com` API

---

## Installation

1. **Clone the Repository** (if hosted on GitHub):
   ```bash
   git clone https://github.com/PavinDas/IPeekaboo.git
   cd IPeekaboo
   ```
2. Install Dependencies
    ```bash
    pip install requests colorama
    ```

---

##Usage

1. Change permission
    ```bash
    chmod +x ipick.py
    ```
2. Run the script
    ```bash
    python3 ipick.py
    ```
3. Follow the Prompt
- Enter an IP address when prompted.
4. Output
```text
[+] CITY         Mountain View
[+] ISP          Google LLC
[+] COUNTRY      United States
[+] REGION       California
[+] TIMEZONE     America/Los_Angeles
[+] ZIP          94035
[+] LATITUDE     37.4056
[+] LONGITUDE    -122.0775
```
5. Stop the script
- Press ```Ctrl+C``` to exit 

---

## Example

```text
$ python ip_lookup.py

@@@  @@@@@@@   @@@   @@@@@@@  @@@  @@@
@@@  @@@@@@@@  @@@  @@@@@@@@  @@@  @@@
@@!  @@!  @@@  @@!  !@@       @@!  !@@
!@!  !@!  @!@  !@!  !@!       !@!  @!!
!!@  @!@@!@!   !!@  !@!       @!@@!@!
!!!  !!@!!!    !!!  !!!       !!@!!!
!!:  !!:       !!:  :!!       !!: :!!
:!:  :!:       :!:  :!:       :!:  !:!
 ::   ::        ::   ::: :::   ::  :::
:     :        :     :: :: :   :   :::

[+]  Creator    :  Pavin Das
[+]  GitHub     :  PavinDas
[+]  Instagram  :  pavin__das

Enter IP Address: 8.8.8.8

[+] CITY         Mountain View
[+] ISP          Google LLC
[+] COUNTRY      United States
[+] REGION       California
[+] TIMEZONE     America/Los_Angeles
[+] ZIP          94035
[+] LATITUDE     37.4056
[+] LONGITUDE    -122.0775
```