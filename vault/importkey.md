## Import Key
### Import key 
* If you want to wrap your key material using RSA_OAEP_AES_SHA256, then you must patch your CLI with a supported OpenSSL patch.
* See :  https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm
### open ssl patch
* Create directories to store the latest OpenSSL binaries in

```
mkdir $HOME/build
mkdir -p $HOME/local/ssl
cd $HOME/build
 
[opc@ctrl .ssh]$ openssl version
OpenSSL 1.0.2k-fips  26 Jan 2017
[opc@ctrl .ssh]$ curl -O https://www.openssl.org/source/openssl-1.1.1d.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8638k  100 8638k    0     0  31.3M      0 --:--:-- --:--:-- --:--:-- 31.3M
[opc@ctrl .ssh]$ tar -zxf openssl-1.1.1d.tar.gz
[opc@ctrl .ssh]$ sudo yum install patch make gcc -y
...
Dependencies Resolved

===========================================================================================================================================================
 Package                          Arch                              Version                                    Repository                             Size
===========================================================================================================================================================
Installing:
 patch                            x86_64                            2.7.1-12.el7_7                             ol7_latest                            110 k

Transaction Summary
===========================================================================================================================================================
Install  1 Package

Total download size: 110 k
Installed size: 210 k
Downloading packages:
patch-2.7.1-12.el7_7.x86_64.rpm                                                                                                     | 110 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : patch-2.7.1-12.el7_7.x86_64                                                                                                             1/1
  Verifying  : patch-2.7.1-12.el7_7.x86_64                                                                                                             1/1

Installed:
  patch.x86_64 0:2.7.1-12.el7_7

```

*   Run the following commands:

```
cat <<-EOF | patch -d $HOME/build/ -p0
diff -ur orig/openssl-1.1.1d/apps/enc.c openssl-1.1.1d/apps/enc.c
--- orig/openssl-1.1.1d/apps/enc.c      
+++ openssl-1.1.1d/apps/enc.c   
@@ -533,6 +533,7 @@
          */

         BIO_get_cipher_ctx(benc, &ctx);
+        EVP_CIPHER_CTX_set_flags(ctx, EVP_CIPHER_CTX_FLAG_WRAP_ALLOW);

         if (!EVP_CipherInit_ex(ctx, cipher, NULL, NULL, NULL, enc)) {
             BIO_printf(bio_err, "Error setting cipher %s\n",
EOF

```

```[opc@ctrl build]$ cat <<-EOF | patch -d $HOME/build/ -p0
diff -ur orig/openssl-1.1.1d/apps/enc.c openssl-1.1.1d/apps/enc.c
> diff -ur orig/openssl-1.1.1d/apps/enc.c openssl-1.1.1d/apps/enc.c
> --- orig/openssl-1.1.1d/apps/enc.c
> +++ openssl-1.1.1d/apps/enc.c
> @@ -533,6 +533,7 @@
>           */
>
>          BIO_get_cipher_ctx(benc, &ctx);
> +        EVP_CIPHER_CTX_set_flags(ctx, EVP_CIPHER_CTX_FLAG_WRAP_ALLOW);
>
>          if (!EVP_CipherInit_ex(ctx, cipher, NULL, NULL, NULL, enc)) {
>              BIO_printf(bio_err, "Error setting cipher %s\n",
> EOF
patching file openssl-1.1.1d/apps/enc.c
[opc@ctrl build]$
```

```
cd $HOME/build/openssl-1.1.1d/
./config --prefix=$HOME/local --openssldir=$HOME/local/ssl
make -j$(grep -c ^processor /proc/cpuinfo)
make install
```

```
[opc@ctrl vault]$ cd $HOME/local/bin/
[opc@ctrl bin]$ echo -e '#!/bin/bash \nenv LD_LIBRARY_PATH=$HOME/local/lib/ $HOME/local/bin/openssl "$@"' > ./openssl.sh
c_rehash  openssl  openssl.sh
[opc@ctrl bin]$ pwd
/home/opc/local/bin
[opc@ctrl bin]$ chmod 755 ./openssl.sh

```


```
oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa --display-name mek_imported --endpoint https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com --key-shape file://./key_shape.json --protection-mode SOFTWARE

${OPENSSL} rand ${KEY_SIZE} > ${AES_KEY}

/home/opc/local/bin/openssl.sh pkeyutl -encrypt -in aeskey -inkey wrappingkey -pubin -out wrappedkey -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256

oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa --display-name mek_imported --endpoint https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com --key-shape file://./key_shape.json --protection-mode SOFTWARE
```
