# AWS_image_version_updater

### Installation script

**Download** `wget https://github.com/nikolaimaz/Aws_version_updater/blob/master/installer.sh` 

**Important** note: installation script will run `sudo apt-get update && sudo apt-get upgrade -y` 

due to Chrome requiring a lot of dependence which are not avoidable.


**What will be installed and created?** 

1) PIP - package managere for python

2) VENV - Virtual environment for python 

3) libxss1 libappindicator1 libindicator7 - libraries

4) Script will create a directory `updater`

5) Download and install the latest version of Chrome

6) Updater script

7) Script will create a virtual environment and install `selenium` for web scraping 

8) You will need to download chrome driver for your version of Chrome from [link](https://chromedriver.chromium.org/downloads) 

**Run installer** `./installer.sh`

**Run script** `python3 updater.py`


## Manual Installation

**Download Version_Updater.py** where you store you’re docker-compose file

`wget https://github.com/nikolaimaz/Aws_version_updater/blob/master/updater.py`

**Download Chrome.deb**

`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

**Installation**

`apt install python3-pip`

`sudo apt install -y libxss1 libappindicator1 libindicator7`

`sudo dpkg -i google-chrome*.deb`

`sudo apt install -y -fsudo apt install python3-venv`

`python3 -m venv venv`

`source ./venv/bin/activate`

`pip install selenium`

**Check version**
`google-chrome --version`

**After checking the version** and satisfying requirements
download Chrome driver for your version from [link](https://chromedriver.chromium.org/downloads),
and  **place where you store script and docker-compose file**

**How it supposed to look like**

        Folder—
                      |-- Version_updater.py
                      |-- chromedriver
                      |-- docker-compose.yml

**Run script**
`python3 updater.py`

## In case of failure

99% failure is caused due to changes  in xpath 

So to fix this issue you have to Copy full XPATH 

1)From image name

2)From button

3)From version or name in image tags

![image](https://user-images.githubusercontent.com/69244449/226070187-c43153aa-cd49-4012-a854-dd4a114c9126.png)

And replace old XPATH in this section

![image](https://user-images.githubusercontent.com/69244449/226070362-34a5adf1-1c1c-4d48-b023-ee6d8db3c788.png)



