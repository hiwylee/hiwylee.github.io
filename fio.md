
## Block Volume Performance
* Read-only
```bash
$ sudo yum install -y fio
[opc@wks ~]$ sudo fio --direct=1 --ioengine=libaio -size=10g --bs=4k --runtime=60 --numjobs=8 --iodepth=64 --time_based --rw=randread --group_reporting --filename=/dev/sda --name=iops-test
iops-test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
...
fio-3.7
Starting 8 processes
Jobs: 8 (f=8): [r(8)][100.0%][r=11.1MiB/s,w=0KiB/s][r=2830,w=0 IOPS][eta 00m:00s]
iops-test: (groupid=0, jobs=8): err= 0: pid=32265: Sun Jul 26 05:48:52 2020
   read: IOPS=3060, BW=11.0MiB/s (12.5MB/s)(719MiB/60172msec)
    slat (usec): min=2, max=215146, avg=2504.13, stdev=10833.66
    clat (usec): min=690, max=864172, avg=164701.59, stdev=104199.41
     lat (usec): min=698, max=875304, avg=167206.37, stdev=105214.36
    clat percentiles (msec):
     |  1.00th=[    7],  5.00th=[   20], 10.00th=[   39], 20.00th=[   74],
     | 30.00th=[   96], 40.00th=[  116], 50.00th=[  155], 60.00th=[  188],
     | 70.00th=[  207], 80.00th=[  253], 90.00th=[  305], 95.00th=[  355],
     | 99.00th=[  456], 99.50th=[  498], 99.90th=[  575], 99.95th=[  609],
     | 99.99th=[  709]
   bw (  KiB/s): min=  471, max= 5407, per=12.31%, avg=1507.33, stdev=501.92, samples=960
   iops        : min=  117, max= 1351, avg=376.72, stdev=125.48, samples=960
  lat (usec)   : 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.04%, 4=0.26%, 10=1.90%, 20=3.13%, 50=7.82%
  lat (msec)   : 100=19.39%, 250=47.13%, 500=19.90%, 750=0.42%, 1000=0.01%
  cpu          : usr=0.07%, sys=1.14%, ctx=48058, majf=0, minf=601
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=99.7%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwts: total=184174,0,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=11.0MiB/s (12.5MB/s), 11.0MiB/s-11.0MiB/s (12.5MB/s-12.5MB/s), io=719MiB (754MB), run=                                         60172-60172msec

Disk stats (read/write):
  sda: ios=184667/15, merge=36/2, ticks=15075999/189, in_queue=7258554, util=95.05%

```
* Write-only : ``-rw=randwrite``
```bash
[opc@wks ~]$ sudo fio --direct=1 --ioengine=libaio -size=10g --bs=4k --runtime=60 --numjobs=8 --iodepth=64 --time_based --rw=randwrite --group_reporting --filename=/dev/sda --name=iops-test
```
* Read/Write Mix : ``-rw=randrw``
```bash
[opc@wks ~]$ sudo fio --direct=1 --ioengine=libaio -size=10g --bs=4k --runtime=60 --numjobs=8 --iodepth=64 --time_based --rw=randrw --group_reporting --filename=/dev/sda --name=iops-test
```
