"""
$Id: $
Network Manager is a tool that is meant to enable Network Manager by pressing only one button.

Our goal is to make your life easier.

If you have any issue or any idea for this programm, contact me: <https://github.com/Th3BrowserPirates/nme-kali-linux.git>

@author TheBrowserPirates <http://thebrowserpirate.weebly.com/>

@date 2018-10-07
@version 1.0.2

@TODO Test in python 3.x

"""
airmon-ng start wlan0
airmon-ng check kill
/etc/init.d/network-manager start
break

