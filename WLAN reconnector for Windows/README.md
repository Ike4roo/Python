# A simple Python script to check if adapter is on
### WLAN adapter reconnector

***
#### If Wi-Fi adapter is off, it lets you to reconnect it again to stay online with your dependent Wi-Fi services.

***
Due to Win 10 (Home / Single Language / Pro / some other non-server versions)  limitations if a wired connection already is up, Wi-Fi goes down despite of your configurations.<br>
If you use some dependent applications that uses both of connections (wired and air) you need to reconnect it manually.<br>
This script lets you to do that automatically. Just schedule it  on boot-on of your machine and give in task sheduler Administrator rights to let it execute correctly:
```CMD
Win+R -> taskschd.msc
```
<br>
Admin rights are needed to work with integrated system library.<br>
Otherwise, you'll see a error message box.

***
GUI TKinter library is used just to be more user-friendly.<br>
You have to be sure it is installed on a machine.<br>
Don't need it? Then, delete from script.

***
Be aware that you need to install Python 3.x and TKinter on a machine to execute it.
Then, please open it and modify ***path***, ***WLAN***, ***SSID*** variables with your own.<br>
<ul>
<li> path - variable is where the script is located,</li>
<li> WLAN - name of your Wi-Fi or LAN connection in Network Manager (rename there if necessary)</li>
<li> SSID - is a name of Wi-Fi you use (machine should be already authorized in it)</li>
</ul>

***
Your Wi-Fi connection should have been named as *WLAN* in your network adapters list!
Otherwise, edit that name in script to your own.


