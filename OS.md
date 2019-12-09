## linux disk low format tools
```bash
$sudo apt-get install dcfldd pv
$ sudo dcfldd if=/dev/zero |pv| sudo dcfldd of=/dev/sda
     (명령)        (소스)   (pv명령)      (재명령)       (타겟)
```
## linux 디스크 삭제
* [https://itgameworld.tistory.com/30](https://itgameworld.tistory.com/30)
### Disk 데이터 완전 삭제
```bash
dd if=/dev/zero of=/dev/sda
```
### Disk MBR  삭제
```bash
dd if=/dev/zero of=/dev/sda count=1 bs=446
```

### Disk 파티션삭제
```bash
dd if=/dev/zero of=/dev/sda count=1 bs=512
```

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
```bash
root@hamonikr:~# vgdisplay
  --- Volume group ---
  VG Name               ol_lobi7u6
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  4
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                3
  Open LV               1
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <237.28 GiB
  PE Size               4.00 MiB
  Total PE              60743
  Alloc PE / Size       60742 / 237.27 GiB
  Free  PE / Size       1 / 4.00 MiB
  VG UUID               l8HCcu-qtof-oUUZ-4qox-lcxa-ER7w-FgMOy2
   
root@hamonikr:~# vgremove ol_lobi7u6
Do you really want to remove volume group "ol_lobi7u6" containing 3 logical volumes? [y/n]: y
  Logical volume ol_lobi7u6/swap in use.

```
