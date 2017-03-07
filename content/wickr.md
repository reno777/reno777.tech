Title: Wickr on Debian Sid
Date: 2017-01-03 17:41
Category: Communications

#When it doesnt work...

Well, I hate to break it to you, but the answer to why wont Wickr work on my Debian sid, is very hard to find. Unless you know specifially what you are doing it may take a couple hours to a 
couple days depending on how hard you look. There was only one post I could find specfically on this matter, and it was only relating to ubunutu. The error code I was getting after installing 
Wickr and running the `wickr-me` command in the terminal was this:

 >`wickr-me: error while loading shared libraries: libgstapp-0.10.so.0: cannot open shared object file: No such file or directory`

So I googled it and came up with [this website](http://askubuntu.com/questions/764235/wickr-2-6-0-4-installed-but-unable-to-open) which again wasnt helpful at all as the apt-get commands it tells
you to run cannot find the correct packages.

###The Fix

After I serached for roughly 2 to 3 hours I finally found the package I needed through the Debian Package Website. Ill save you some time and the frustration of trail and error and post the 
specific link [here.](https://packages.debian.org/wheezy/amd64/libgstreamer-plugins-base0.10-0/download) Just click on the link on the website that says "security.debian.org/debian-security" and
it should automatically open a download que. Once it has downloaded, make sure you are in the folder that its in go ahead and run 
```
dpkg -i libgstreamer-plugins-base0.10-0_0.10.36-1.1+deb7u1_amd64.deb
```  
After that, all I did was run the `wickr-me` command again and it popped right up.

Hope this helped out! If there are any questions or mistakes be sure to [Contact](../pages/contact.html) me. I plan on adding a comments area soon.
