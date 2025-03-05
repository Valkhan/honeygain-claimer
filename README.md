# honeygain-claimer

Honeygain script to claim daily rewards

# Requirements

- Python 3
- Honeygain account
- Selenium
- Chrome browser
- Chrome driver

# Installation

Assuming you have Python 3 installed, you can install the required packages by running:

```bash

# Create a virtual environment called venv-honeygain
python3 -m venv venv-honeygain

# Activate the virtual environment

# On Windows
venv-honeygain\Scripts\Activate.ps1

# On Linux
source venv-honeygain/Scripts/activate

# Install the required packages
pip install -r requirements.txt

```

## Chrome driver

You can download the Chrome driver from [here](https://googlechromelabs.github.io/chrome-for-testing/) and place the .exe at the root of the project, eg: `./chromedriver.exe`

You may also check on your Chrome version by going to `chrome://settings/help` and download the corresponding version of the Chrome driver in the given link:

- For example, if you have Chrome version 133.0.6943.142 on windows, you can download the Chrome driver from this link:
https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.142/win64/chromedriver-win64.zip

# Usage

Copy the `.env.example` file to `.env` and fill in the required fields.

```bash
# After initializing the virtual environment, run the script
python claim.py
```

# Disclaimer

I am not responsible for any misuse of this script. Use it at your own risk.
The only warranty is that this script won't use your Honeygain account to do anything other than claim the daily rewards neither it will store your credentials.
