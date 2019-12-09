### how to remove linux os grub 
```bash
# cat  /etc/apt/apt.conf
Acquire::http::Proxy  "http://www-proxy.us.oracle.com:80";
Acquire::https::Proxy "http://www-proxy.us.oracle.com:80";

sudo add-apt-repository ppa.yannubuntu/boot-repair 
 apt update


apt-get install os-uninstaller
os-uninstaller 

```
