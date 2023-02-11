sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install  python3-pip -y
sudo apt-get install python3-venv -y
sudo apt install -y libxss1 libappindicator1 libindicator7 -y
mkdir updater
cd updater
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
wget https://github.com/nikolaimaz/Aws_version_updater/blob/master/updater.py
python3 -m venv venv
source ./venv/bin/activate
pip3 install selenium
sudo dpkg -i google-chrome*.deb
sudo apt install -y -f
clear
echo 
echo "please download chromedriver for "
 google-chrome --version
echo 
