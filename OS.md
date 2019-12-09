### Linux Mint Partition Basic
```
root@wylee-lnx:/boot# df
Filesystem     1K-blocks     Used Available Use% Mounted on
udev            16332768        0  16332768   0% /dev
tmpfs            3273172     2852   3270320   1% /run
/dev/sda3       38186520 12129188  24087824  34% /
tmpfs           16365848   134756  16231092   1% /dev/shm
tmpfs               5120        4      5116   1% /run/lock
tmpfs           16365848        0  16365848   0% /sys/fs/cgroup
/dev/sda2          96138        1     96137   1% /boot/efi
/dev/sda4      921835620  6344076 868595092   1% /home
tmpfs            3273168       28   3273140   1% /run/user/1000

```
```
Command (m for help): p

Disk /dev/sda: 931.5 GiB, 1000204886016 bytes, 1953525168 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: 1F952A9F-D080-46A8-8483-A42F7BEE8E13

Device        Start        End    Sectors   Size Type
/dev/sda1        34       1987       1954   977K BIOS boot
/dev/sda2      1988     197300     195313  95.4M Microsoft basic data
/dev/sda3    197301   78322301   78125001  37.3G Linux filesystem
/dev/sda4  78322302 1953525118 1875202817 894.2G Linux filesystem

```
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
