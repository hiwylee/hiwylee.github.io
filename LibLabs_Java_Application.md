## Using OCI to Build a Java Application
* [Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=690&p210_type=3&session=104091697673337)
### Lab 1: Env
* Java env
  * fixes the "LC_CTYPE: cannot change locale" warning,
  * installs various tools (git, tree, bat)
  * installs the latest OpenJDK version,
  * installs Apache Maven,
  * installs the Helidon CLI,
  * configures the VM firewall to open the 8080 port,
  * handles some miscellaneous details (ex. setting the path).

```bash
[opc@ctrl ~]$ source <(curl -L https://gist.githubusercontent.com/delabassee/a11e09dcf5a85dae87a5fd6a96ce77ea/raw/ed200268f5d6cdcbb2a9f16d91e5b5f23a4a682e/vm-setup.sh)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2958  100  2958    0     0   3485      0 --:--:-- --:--:-- --:--:--  3488

*** URLs ***

-> https://download.java.net/java/GA/jdk15/779bf45e88a44cbd9ea6621d33e33db1/36/GPL/openjdk-15_linux-x64_bin.tar.gz
-> https://downloads.apache.org/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
-> https://github.com/oracle/helidon-build-tools/releases/download/2.1.0/helidon-cli-linux-amd64

*** Installing git, tree, bat... ***

Loaded plugins: langpacks, ulninfo
ol7_UEKR5                                                                                                                       | 2.8 kB  00:00:00
ol7_addons                                                                                                                      | 2.8 kB  00:00:00
.....

*** Installing OpenJDK 15... ***

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
...
*** Installing Maven... ***

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 9283k  100 9283k    0     0  2890k      0  0:00:03  0:00:03 --:--:-- 2891k
apache-maven-3.6.3/README.txt
apache-maven-3.6.3/LICENSE
....

*** Installing Helidon CLI... ***

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   649  100   649    0     0    184      0  0:00:03  0:00:03 --:--:--   184
100 16.8M  100 16.8M    0     0  2567k      0  0:00:06  0:00:06 --:--:-- 6588k

*** Configuring firewall for port 8080... ***
success
success
build.date      2020-08-25 23:30:11 UTC
build.version   2.1.0
build.revision  47761c80
....
```

### Lab 2: Exploring Helidon

### Lab 3: Java SE Preview Features

### Lab 4: The Conference Application

### Lab 5: Text Blocks

### Lab 6: Records

### Lab 7: Sealed Classes

### Lab 8: Sealed Classes

### Lab 9: Pattern Matching for instanceof

### Lab 10: jlink
