## cpu count 확인
* linux

```bash
[opc@rac1 ~]$ sudo  dmidecode -t processor
# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 2.8 present.

Handle 0x0400, DMI type 4, 42 bytes
Processor Information
        Socket Designation: CPU 0
        Type: Central Processor
        Family: Other
        Manufacturer: QEMU
        ID: 54 06 05 00 FF FB 8B 0F
        Version: pc-i440fx-2.9
        Voltage: Unknown
        External Clock: Unknown
        Max Speed: 2000 MHz
        Current Speed: 2000 MHz
        Status: Populated, Enabled
        Upgrade: Other
        L1 Cache Handle: Not Provided
        L2 Cache Handle: Not Provided
        L3 Cache Handle: Not Provided
        Serial Number: Not Specified
        Asset Tag: Not Specified
        Part Number: Not Specified
        Core Count: 2
        Core Enabled: 2
        Thread Count: 2
        Characteristics: None
```

```
[opc@rac1 ~]$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    2
Core(s) per socket:    2
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 85
Model name:            Intel(R) Xeon(R) Platinum 8167M CPU @ 2.00GHz
Stepping:              4
CPU MHz:               1995.263
BogoMIPS:              3990.62
Virtualization:        VT-x
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              4096K
L3 cache:              16384K
NUMA node0 CPU(s):     0-3
...
```
