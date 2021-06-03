# firefox-backgroundimg-swaper
  
You can use this script to set the background image of your mozilla firefox browser and make computer randomly choosing one of pictures you provided.

# Setup
1. Go to about:support in the address bar. View the section "Application Basics" ➔ Profile Directory (or "Profile Folder" on MacOS) ➔ click the button "Open Directory" (or "Show in Finder" on MacOS)
2. Create a directory called chrome inside the opened directory, if it's not already there.
3. Go to the chrome directory and create a directory called __img__. Move your image to the img directory.
4. Now you could `git clone` the repo to the chrome folder
5. Make `swapimage.py` executable and add to crontab

# For those who love copy pasting :wink:

Inside profile directory:

```bash
mkdir chrome
cd chrome
git clone https://github.com/miki164/firefox-backgroundimg-swaper.git .
chmod +x swapimage.py
sudo crontab -e
```
Now you have to add crontab entry. Here it's a very useful [Link](https://crontab.guru/)

In my case working somethnig like that:
```
SHELL=/bin/bash
@reboot ~/.mozilla/firefox/aolcyudt.default-release/chrome/swapimage.py  ~/.mozilla/firefox/aolcyudt.default-release/chrome/img/
```
