## Import Key
* reference : https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm
### .인스턴스 설정 (instance pricipal)
* daynamic group 생성
  * Any {instance.id = 'ocid1.instance.oc1.ap-seoul-1.anuwgljrio3ypnycemo43yjdf3hkfkcfe6zjrop5k7cffdk3g3pobdzbqlta'}	
* Policy 설정
  * Allow dynamic-group vault to manage all-resources in compartment sandbox-poc	
* oci cli auth 설정
  * 
### Import key 
* If you want to wrap your key material using RSA_OAEP_AES_SHA256, then you must patch your CLI with a supported OpenSSL patch.
* See :  https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm
* ``Open SSL 1.1.1 및 os patch 필요`` 
   * https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm#unique_1658146802
* [``wrapped_key(base64) import시 주의 사항``](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys.htm#unique_1658146802)
   * wrapped_import_key.json 에서  "keyMaterial" 값(bases64 wrappedkey)을 줄떄 newline 이 있으면 제거해야 됨

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
### key gen
* openssl 1.1.1 & os patch 후에
```
 ${OPENSSL} rand ${KEY_SIZE} > ${AES_KEY}
```

### wrapping key (pubkey)
* console 에서 import custom key 에서 볼 수 있음

```
key_text=$(oci kms management wrapping-key get --endpoint $VAULT_KEYMANAGEMENT_ENDPOINT | grep public-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')
```

### wrappkey ( key wrapped with pubkey)

```
${OPENSSL}  pkeyutl -encrypt -in aeskey -inkey wrappingkey -pubin -out wrappedkey -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256
```

### 설정파일 

* keyMaterial : 값에 new line 이 있으면 안됨.
```
key_material=$(${BASE64} ${WRAPPED_KEY})
echo "{ \"wrappingAlgorithm\": \"RSA_OAEP_SHA256\", \"keyMaterial\": \"${key_material}\" }" > wrapped_import_key.json
echo "{ \"algorithm\": \"AES\", \"length\": ${KEY_SIZE} }" > key_shape.json
```

* ``wrapped_import_key.json 에서 new line 제거`` 

```
cat key_shape.json
{ "algorithm": "AES", "length": 32 }

cat wrapped_import_key.json

{ "wrappingAlgorithm": "RSA_OAEP_SHA256", "keyMaterial": "VAW8ABoKySqb4bRoc5B3Ceex/PsV5jSSkifo3knzYWGokvNm/OZtkGdHP4SjegLWnchEoPax1+D3E3eHhJbG16Vcd/54RyO6ZSjrEdi9khD9/o7kTCzWs8bkh/M4iCsJFJX5ETmgx1X95tGJWR/T+XTiGZVDaiiNGMTjv36WBDfU9jDEHFAynm8MyMnRtroj+GPO3pOcYDB+OZsz5Hmgjtq3boyFfKAXZtBjqUIOpqkksxKuqScTDLD5LrtqqzRynko9OgNiNJxje0IaUIagju3xfqgXBvxv5qJgXti8xzPSR5r/B9pMONxWl/MIzPsOfdJvEFwu2hsC0T9FfgR1n4wVpKfK3x0HES1hVu2rF1LavZNJsXFCvbGJig/r4UDo0QR+JndvvIYNkTp5H6G2Hll3RsDXU9wURcv1fq6EMC7xUHowq1rYI7cNVMvKtELC5WMwHFjdpTKL7gMAA7RCM5DC3MX9hNgioPWW4MTq10++VDPjzmdinm8z1b1fDpKGxBCbJCUB8I5u1Lg0RCdmzf5i3pe0lxai/nnfUiQC/PB+TkY2KrFCoJBpSjIcLUYKQwW+C9s32i50VQTFFugQ/6ZnLnLGDAFQg0kwYbMmTLL6PQ2eAnrY7wySe4uQZRyGeprvOb4H6G9sOHkOCsr34Aj4c7b1wY78tWKU1l7KUAg=" }
```

### import wrappkey (base64)

```
oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa --display-name mek_imported --endpoint https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com --key-shape file://./key_shape.json --protection-mode SOFTWARE
{
  "data": {
    "compartment-id": "ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa",
    "current-key-version": "ocid1.keyversion.oc1.ap-seoul-1.cnqtaqh2aagiu.dcqsmey3mdyaa.abuwgljrf4yremea2t3hmvuijosr7jly3cda3lgi3ggi3pb2ho3257a3zmca",
    "defined-tags": {},
    "display-name": "mek_imported",
    "freeform-tags": {},
    "id": "ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrvw2g2ct37a6vh6cs3tqof725urbmh4retim6svwpoj6j5dkhddcq",
    "is-primary": true,
    "key-shape": {
      "algorithm": "AES",
      "curve-id": null,
      "length": 32
    },
    "lifecycle-state": "CREATING",
    "protection-mode": "SOFTWARE",
    "replica-details": null,
    "restored-from-key-id": null,
    "time-created": "2021-09-03T05:43:44.217000+00:00",
    "time-of-deletion": null,
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrktxtvdrfpyykgc4cy7bbtavmaive2poxvucf6bje5hbuyxhtjmoq"
  },
  "etag": "4bcd50f6cdbb2fcf1f1554932895687aebe1e0d6"
}
```


<!--
### 환경설정 
```
OPENSSL="/home/opc/local/bin/openssl.sh"
AES_KEY="aeskey"
WRAPPING_KEY="wrappingkey"
WRAPPED_KEY="wrappedkey"
VAULT_KEYMANAGEMENT_ENDPOINT="https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com"
COMPARTMENT_ID="ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa"
DISPLAY_NAME="mek_imported"
KEY_SIZE="32" # Specify 16 (for 128 bits), 24 (for 192 bits), or 32 (for 256 bits).
# PROTECTION_MODE either SOFTWARE or HSM
PROTECTION_MODE="SOFTWARE"
BASE64="base64"
```

## Export Key
* reference :https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/exportingkeys.htm

### 

```
# key name : mek_imported

OPENSSL="/home/opc/local/bin/openssl.sh"

KEY_OCID=ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrvw2g2ct37a6vh6cs3tqof725urbmh4retim6svwpoj6j5dkhddcq
ENCRYPTION_ALGORITHM="RSA_OAEP_AES_SHA256"
VAULT_CRYPTO_ENDPOINT=https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com
PUBLIC_KEY_STRING="`cat  wrappingkey.imsi`"


PRIVATE_KEY_PATH="prikey" # The location of the private key.
SOFTWARE_KEY_PATH="mek" # The location for outputting the software-protected master encryption key.
TEMP_AES_KEY_PATH="tempAes" # The location for outputting the temporary AES key.
TEMP_WRAPPED_AES_PATH="tempWrappedAES" # The location for outputting the wrapped temporary AES key.
WRAPPED_SOFTWARE_KEY_PATH="WrappedMEK"

oci kms crypto key export --key-id  ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}"  --endpoint ${VAULT_CRYPTO_ENDPOINT}

wonyong_le@cloudshell:exp (ap-seoul-1)$ oci kms crypto key export --key-id  ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}"  --endpoint ${VAULT_CRYPTO_ENDPOINT}
{
  "data": {
    "algorithm": "RSA_OAEP_AES_SHA256",
    "encrypted-key": "jHaOhGMzgbb9lRMkfiN+QfnHMbNXXI25CJt6ij8YSaZpDA3NINFtyT+VFh9k0d5IFAQNToi2rKCQIcwZbVHsJPUkjtkXk10q5NQq29prz9qr8FBic22Z7w7Rwi9IAY7Bx//yrraTaBmmjyj+i2qflu+kOWwRkrDHGf8FzO6nx25TGQDnpR5bZY2QvyT66Y40lfpNITuL/8cPkeFXcDlLkLud6lWDqgNI/FAH9ukwc2TDDEigyYz/vRT91G1atmSfnSVdLzqvD8yNUALTS7hwtbBsLvBlIg/74Wg6McpJc8TNdJ+w/zEECkXMZx9SS6KTTfIXBIXvM7lxtvoqqlp1pw5Z+UOs3KoD1bIdSZvKqvu/qPFhTxYbhSKmAVTViRdXmFsS6DdysZhQSHq9yv1jS+plrKhaP22AFMIrPBa3lRHHFBrw3PPHLcwX6jBzpuQBtDWqiVy30aesL/S7+J9QT6aSm+S/xuZ6Nhac3u82Kp1O/LaXgC8EM/wcKKzeNCcTozbmT8PDCcJ3COn27W9ywiAincjpVXw9gl38LdyqC6VckzDncXdb3mnMbt/Ps3mOSSW2GAWn2omCqa7BJAscvpcFoRsAxvLxJXyZ6LS1djl9bkz9aSL7EdsqIN8TDOi+g3AK2kPzngZzOa3JQjY5NjcIjVwkY+7tKlIiQIsAcpnmbnmTPlUc1LBgBmqyeJ1GkLGophivrazZYUpO9HFh2FP9FeUINJGj",
    "key-id": "ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrvw2g2ct37a6vh6cs3tqof725urbmh4retim6svwpoj6j5dkhddcq",
    "key-version-id": "ocid1.keyversion.oc1.ap-seoul-1.cnqtaqh2aagiu.dcqsmey3mdyaa.abuwgljrf4yremea2t3hmvuijosr7jly3cda3lgi3ggi3pb2ho3257a3zmca",
    "time-created": "2021-09-03T05:43:44.238000+00:00",
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrktxtvdrfpyykgc4cy7bbtavmaive2poxvucf6bje5hbuyxhtjmoq"
  }
}
```

*  extract key part only
```
 oci kms crypto key export --key-id  ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}"  --endpoint ${VAULT_CRYPTO_ENDPOINT} | grep encrypted-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g'
sOYuP3RG8vRrWGv4nXEw9ocEnoBQtuTejfn42Kb8BOhuk19BNWrb2z53r+dUt3XcY/EgI0lnTEocvANHbSntQ0uCuEQlesAEIIBg9DTmoG8o/458Tp3GaXGNKValZPq7KxpAhEgOtdAGTjF16u+xd0FZ7z6XJasC69CfVU9N+JQ9NtmzxQNUCn/O2qGRfiP8AdRyxK7SYM0vtuST8OKJWVTUMRlpymnqEHFu94gMZO3gL7ggStYt3dqHnDU7WPehhouQ8vd9gbyTp6zWCwa/0aCl3lJT7UzSRbKmxCxb4vlqA2S2jRzeQHLSkXjvXyI6zAdXbqbY+Mk4fG8JnC+PuwRNoR+itPgR2kdpnC5pcmKlNgJBU3Cx5Q+hZoPcsB5zsIk1TJVLeYLhNxao8k6E5H70uTDT9KZldBgoZ1SXrJoIMVjbrigNZ4w2E3QCVt0iAKS0J2DgKe62oDoXOzO95T/0FU6ht0cdfORboiixvWNfJOtZGGNCRg4FXcKiTQc8TIRyZ7/JTuDG1gAz3e3KpGrdsTnLbOzwiwD9/nHAr4e6cXoufnS3XQF2RhoTW3mY6mG+8zRZXxai251XQ30A99F4ueFE5GNdOmhvH+9TFDNaCuDjTdxEZFdRxENd6E4smvLGVXHCl68W9fIP+gB9y1aH+Began76tF0osnPfpz/gIopuGUphb2jfPLazW4MFVzAAa7wxymT03XbsHFRonTwS7qcsNQys
```

```
wrapped_data=$(oci kms crypto key export --key-id  ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}"  --endpoint ${VAULT_CRYPTO_ENDPOINT} | grep encrypted-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')
wrapped_data=$(oci kms crypto key export --key-id  ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}"  --endpoint ${VAULT_CRYPTO_ENDPOINT} | grep encrypted-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')
```

## decode wrappedkey

```
# Decode the encoded wrapped data and convert it to hexadecimal format.
wrapped_data_hex_array=(`echo ${wrapped_data} | base64 -d | xxd -p -c1`)
wrapped_data_hex_array_length=${#wrapped_data_hex_array[*]}

```
-->
