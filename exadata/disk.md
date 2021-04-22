### Disk 확인

```
CellCLI> list cell
         krx8maceladm01  online

CellCLI> LIST CELLDISK
         CD_00_krx8maceladm01    normal
         CD_01_krx8maceladm01    normal
         CD_02_krx8maceladm01    normal
         CD_03_krx8maceladm01    normal
....
         FD_02_krx8maceladm01    normal
         FD_03_krx8maceladm01    normal
..
         PM_11_krx8maceladm01    normal

```

* HardDisk

```

CellCLI> LIST CELLDISK CD_00_krx8maceladm01 detail
         name:                   CD_00_krx8maceladm01
         comment:
         creationTime:           2021-03-09T08:00:05+09:00
         deviceName:             /dev/sdc
         devicePartition:        /dev/sdc
         diskType:               HardDisk
         errorCount:             0
         freeSpace:              0
         id:                     c0e1463f-fc1d-46ea-ba4c-f9f6f654ea98
         physicalDisk:           N3DEJT
         size:                   12.4737091064453125T
         status:                 normal
```
* FlashDisk

```
CellCLI> LIST CELLDISK FD_00_krx8maceladm01 detail
         name:                   FD_00_krx8maceladm01
         comment:
         creationTime:           2021-03-09T08:00:06+09:00
         deviceName:             /dev/md310
         devicePartition:        /dev/md310
         diskType:               FlashDisk
         errorCount:             0
         freeSpace:              0
         id:                     e8a3926b-0e76-44cc-b2f9-0ad7c3b2fdf8
         physicalDisk:           PHLN943301MJ6P4EGN-2,PHLN943301MJ6P4EGN-1
         size:                   5.8218994140625T
         status:                 normal

* PMEM

```

CellCLI> LIST CELLDISK PM_11_krx8maceladm01 detail
         name:                   PM_11_krx8maceladm01
         comment:
         creationTime:           2021-04-01T10:45:18+09:00
         deviceName:             /dev/dax7.0
         devicePartition:        /dev/dax7.0
         diskType:               PMEM
         errorCount:             0
         freeSpace:              848M
         id:                     70cd9bda-4d79-4fa0-a937-a1c2cb4a7064
         physicalDisk:           8089-a2-1943-00000184
         size:                   125.984375G
         status:                 normal

```
