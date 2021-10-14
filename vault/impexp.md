## IMP / EXP encryped with my own keypair

### ENV

```bash
OPENSSL="/home/opc/local/bin/openssl.sh"
AES_KEY="aeskey"
WRAPPING_KEY="wrappingkey"
WRAPPED_KEY="wrappedkey"
VAULT_KEYMANAGEMENT_ENDPOINT="https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com"
COMPARTMENT_ID="ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa"
DISPLAY_NAME="mek_final"
KEY_SIZE="32" # Specify 16 (for 128 bits), 24 (for 192 bits), or 32 (for 256 bits).
# PROTECTION_MODE either SOFTWARE or HSM
PROTECTION_MODE="SOFTWARE"
BASE64="base64"

if [[ $(uname -s) == "MINGW"* ]]
then
    BASE64="base64 -w0";
fi


#
# Generate an AES key.
#
# Use OpenSSL to generate an AES key of ${KEY_SIZE} bytes.
# You can use any source for your AES key.
#
${OPENSSL} rand ${KEY_SIZE} > ${AES_KEY}
#
# Ask the Vault service for the public wrapping key by using
# the vault's key management endpoint.
# The public key is stored as ${WRAPPING_KEY}.
#
key_text=$(oci kms management wrapping-key get --endpoint $VAULT_KEYMANAGEMENT_ENDPOINT | grep public-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')
echo -e $key_text > ${WRAPPING_KEY}
#
# Wrap the AES key by using RSA-OAEP with SHA-256.
#
${OPENSSL} pkeyutl -encrypt -in ${AES_KEY} -inkey ${WRAPPING_KEY} -pubin -out ${WRAPPED_KEY} -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256
#
# Import the wrapped key to the Vault service after base64 encoding the payload.
#
# The service will provide a JSON document containing key details.
#
key_material=$(${BASE64} ${WRAPPED_KEY})
${BASE64} ${WRAPPED_KEY} > ${WRAPPED_KEY}.b64
echo "{ \"wrappingAlgorithm\": \"RSA_OAEP_SHA256\", \"keyMaterial\": \"${key_material}\" }" > wrapped_import_key.json
echo "{ \"algorithm\": \"AES\", \"length\": ${KEY_SIZE} }" > key_shape.json

```

* ``edit wrapped_import_key.json ( remove new line )``

```
 cat wrapped_import_key.json
{ "wrappingAlgorithm": "RSA_OAEP_SHA256", "keyMaterial": "BgNsYWCzjpgqExu/m271BY1qieOgIr4xIYXYxKWvli7iQ1Dv2uXQGow9OeKJiAGHfBWxE34OVrgfaZ87WAbgIT6UpASKsXfs9EZjKuz9EUVSyoZIVQnYXNnA0xXoJlhg06diSIdKSoSni4n8Ddhb0jEVRzct12Kv/LZ2lv/Jxpyj2xQyzeGaqk0vorwgb76xTS3KM6GikGVHjMU8awCBEXzo8JtDRvaJdv/jlN3qRWAGJjZ5leoAHI+pMBCXDD8rJsx/Hqpr45yX12V6cItV4mG5FqpRT6n1wYFcfPuu71A7UipDc/3DkgewMM4HkY6pVi+CHEk1SuGUSzbi2m7r+HEHiD1AGuoWrgYQhpowcuK6YSD+wRz49jyHDyvO98dQIn+jAk50+Mj72lYAz5ELY2FA9KhyC/W2yZQyzXKrgDWanzWHl1DatNA2rCuOx0m/gv+INvd04suTFQp6Oa4JYO8Tgovx2yVoy1a8SeFOKmcWeD9bizwftwluTSPOn7oz9L115Zg2keys857Bepes4t4aUefrKQ5S6Ykayqf9qZ4FZkO/KXUwk8oH9pwly4D0y4Scbv6cSKDJL3JJ7tkIQB1w8axz5L85u2+D2YFG748ArsMWalv12cQwgW3IIloaLHhEB/eXtyKP3KY30SAYmMnNqZMqwh0MrTMDv6XIjIQ=" }
```

* import key

```
oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ${COMPARTMENT_ID} --display-name ${DISPLAY_NAME} --endpoint ${VAULT_KEYMANAGEMENT_ENDPOINT} --key-shape file://./key_shape.json --protection-mode "${PROTECTION_MODE}"
```

### IMP

```
oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa --display-name mek_final --endpoint https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com --key-shape file://./key_shape.json --protection-mode SOFTWARE
{
  "data": {
    "compartment-id": "ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa",
    "current-key-version": "ocid1.keyversion.oc1.ap-seoul-1.cnqtaqh2aagiu.dcqsme3rnhyaa.abuwgljrh52oqfc3trcp5tmdrvtfwlyinre6hgkdwlmmwgtdhdibopiwh4xa",
    "defined-tags": {},
    "display-name": "mek_final",
    "freeform-tags": {},
    "id": "ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrltwjp2vbwpnkhwsvfdpqnxjywa4sml5orisz5tzwjadtad4dnkza",
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
    "time-created": "2021-09-07T07:37:04.196000+00:00",
    "time-of-deletion": null,
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrktxtvdrfpyykgc4cy7bbtavmaive2poxvucf6bje5hbuyxhtjmoq"
  },
  "etag": "ec7fd2ce5c7d21025805eaae5728039d86da8236"
}

```

## Export Key

### Env

* key_ocid : ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrltwjp2vbwpnkhwsvfdpqnxjywa4sml5orisz5tzwjadtad4dnkza

* Generate key pair

```
#
# Generate key pair
#
private_key_path=private.pem
public_key_path=public.pem
rsa_key_size=4096

#
# Generate key pair
#

OPENSSL="/home/opc/local/bin/openssl.sh"

rm ${public_key_path}  ${private_key_path}

${OPENSSL} genrsa -out ${private_key_path} ${rsa_key_size}
${OPENSSL} rsa -in ${private_key_path} -outform PEM -pubout -out ${public_key_path}


[opc@ctrl exp]$ ${OPENSSL} genrsa -out ${private_key_path} ${rsa_key_size}
Generating RSA private key, 4096 bit long modulus (2 primes)
...........................................................................................................++++
...................................................................................................................++++
e is 65537 (0x010001)
[opc@ctrl exp]$ ${OPENSSL} rsa -in ${private_key_path} -outform PEM -pubout -out ${public_key_path}
writing RSA key
```

* env

```
KEY_OCID="ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrltwjp2vbwpnkhwsvfdpqnxjywa4sml5orisz5tzwjadtad4dnkza"

ENCRYPTION_ALGORITHM="RSA_OAEP_SHA256"
VAULT_CRYPTO_ENDPOINT="https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com"
PUBLIC_KEY_STRING="`cat ${public_key_path}`"

PRIVATE_KEY_PATH=${private_key_path} # The location of the private key.

SOFTWARE_KEY_PATH="mek" # The location for outputting the software-protected master encryption key.
TEMP_AES_KEY_PATH="tempAes" # The location for outputting the temporary AES key.
TEMP_WRAPPED_AES_PATH="tempWrappedAES" # The location for outputting the wrapped temporary AES key.
WRAPPED_SOFTWARE_KEY_PATH="WrappedMEK"

VAULT_CRYPTO_ENDPOINT="https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com"
OPENSSL="/home/opc/local/bin/openssl.sh"
```

* note : public key 는 new line 없이 문자열로

### Exp

```
oci kms crypto key export --key-id ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}" --endpoint ${VAULT_CRYPTO_ENDPOINT}
{
  "data": {
    "algorithm": "RSA_OAEP_AES_SHA256",
    "encrypted-key": "l45u6X63SA1BkQB/n9AJybgJtdKqMHBrA11GRLXMt9j0YECvmJ0EnAJvuotqnW7wHWKvrTDd77VsHYrXUxVl59HEjqcIWnLsslpCF2CJDNpQfEup85r/f58wg1Abjmmc7U3tKQ2kD9SzssZXhz1SgayD4oquybPDgIYGkCSUMuLmXZCWFoQ0KnUotKVVc2E9vU0Gt7FtQLIALLtsb29gnwo2XbAKdUhejDmQKXaUnCejA3D4ZU7lYbsLW7LzycdorVFOr9IhhUf+wQoYTtWhADJOtWzMOhNiguJCLDd23XeLcFfgayjICjl9Q7sYX0WICE/zr/R/3elx0vTN17iAvPR6HfCXtNskeF6pDRaRudJ8H0Wuq0sgOg6M0gqsKZgy36lywOXd6BDaY6SfWob+lPEH5hUVAprPxVV7TNnVuJDBbKfh++OWE1IR0fnABbmW4+WyAwRgiddOl9P2PB2ZXMo2ZGGy5tSm4PhVNFCciFAkHXHDaLa3A/yf+kl4UAnwODHGmIAm1AMgYCprQ+9wd+HGkC9G3+GmjBB+bAMrA5QUGQATJCm01yqgV0SU2uhiZNuwjdmCQib29oMWtcq0jA7oUbdgqmau7Ko2GOt+6d2SsZa+Gdti8sxYJk3dI0Q2RYZyHpGO/wHd7TMNXP+yC/ezKRhVbYnXs6f6kIMfPqTDB49K0AUP9BChAg0rnhsF3cuzaaMqzlLTyTruxjidVT9Yzj6GWdfs",
    "key-id": "ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrltwjp2vbwpnkhwsvfdpqnxjywa4sml5orisz5tzwjadtad4dnkza",
    "key-version-id": "ocid1.keyversion.oc1.ap-seoul-1.cnqtaqh2aagiu.dcqsme3rnhyaa.abuwgljrh52oqfc3trcp5tmdrvtfwlyinre6hgkdwlmmwgtdhdibopiwh4xa",
    "time-created": "2021-09-07T07:37:04.216000+00:00",
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrktxtvdrfpyykgc4cy7bbtavmaive2poxvucf6bje5hbuyxhtjmoq"
  }
}

```

* base64 decode

```
wrapped_data=$(oci kms crypto key export --key-id ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}" --endpoint ${VAULT_CRYPTO_ENDPOINT} | grep  encrypted-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')

echo ${wrapped_data} | base64 -d > ${WRAPPED_SOFTWARE_KEY_PATH}
```

* Unwrap the key

```
# Unwrap the wrapped software-protected key material by using the private RSA wrapping key.
 ${OPENSSL} pkeyutl -decrypt -in ${WRAPPED_SOFTWARE_KEY_PATH} -inkey ${PRIVATE_KEY_PATH} -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -pkeyopt rsa_mgf1_md:sha256 -out ${SOFTWARE_KEY_PATH}
Public Key operation error
140283134453568:error:0406506C:rsa routines:rsa_ossl_private_decrypt:data greater than mod len:crypto/rsa/rsa_ossl.c:401:
```

### FULL SCRIPT
#### imp.sh

```
#!/usr/bin/env bash
#
# This script is for demonstration purposes only. It provides
# a functioning set of calls to show how to import AES keys 
# into the Vault service.
#
set -x
OPENSSL="/home/opc/local/bin/openssl.sh"
AES_KEY="aeskey"
WRAPPING_KEY="wrappingkey"
WRAPPED_KEY="wrappedkey"
VAULT_KEYMANAGEMENT_ENDPOINT="https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com"
COMPARTMENT_ID="ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa"
DISPLAY_NAME="mek_final3"
KEY_SIZE="32" # Specify 16 (for 128 bits), 24 (for 192 bits), or 32 (for 256 bits).
# PROTECTION_MODE either SOFTWARE or HSM
PROTECTION_MODE="SOFTWARE"
BASE64="base64"
if [[ $(uname -s) == "MINGW"* ]]
then
    BASE64="base64 -w0";
fi

#
# Generate key pair
#


# ${OPENSSL} genrsa -out ${private_key_path} ${rsa_key_size} 
# ${OPENSSL} rsa -in ${private_key_path} -outform PEM -pubout -out ${public_key_path}
# rm wrappingkey
# ln -s public.pem wrappingkey


#
# Generate an AES key.
#
# Use OpenSSL to generate an AES key of ${KEY_SIZE} bytes.
# You can use any source for your AES key.
#
${OPENSSL} rand ${KEY_SIZE} > ${AES_KEY}
#
# Ask the Vault service for the public wrapping key by using 
# the vault's key management endpoint.
# The public key is stored as ${WRAPPING_KEY}.
#
key_text=$(oci kms management wrapping-key get --endpoint $VAULT_KEYMANAGEMENT_ENDPOINT | grep public-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')
echo -e $key_text > ${WRAPPING_KEY}
#
# Wrap the AES key by using RSA-OAEP with SHA-256.
#
${OPENSSL} pkeyutl -encrypt -in ${AES_KEY} -inkey ${WRAPPING_KEY} -pubin -out ${WRAPPED_KEY} -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256
#
# Import the wrapped key to the Vault service after base64 encoding the payload.
#
# The service will provide a JSON document containing key details.
#
key_material=$(${BASE64} ${WRAPPED_KEY})

${BASE64} ${WRAPPED_KEY} > ${WRAPPED_KEY}.b64

echo "{ \"wrappingAlgorithm\": \"RSA_OAEP_SHA256\", \"keyMaterial\": \"${key_material}\" }" > wrapped_import_key.json
echo "{ \"algorithm\": \"AES\", \"length\": ${KEY_SIZE} }" > key_shape.json
oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ${COMPARTMENT_ID} --display-name ${DISPLAY_NAME} --endpoint ${VAULT_KEYMANAGEMENT_ENDPOINT} --key-shape file://./key_shape.json --protection-mode "${PROTECTION_MODE}"
```

#### exp.sh

```
#!/usr/bin/env bash
#
set -x 

private_key_path=private.pem
public_key_path=public.pem
rsa_key_size=4096

#
# Generate key pair
#

OPENSSL="/home/opc/local/bin/openssl.sh"

rm ${public_key_path}  ${private_key_path} 

${OPENSSL} genrsa -out ${private_key_path} ${rsa_key_size}
${OPENSSL} rsa -in ${private_key_path} -outform PEM -pubout -out ${public_key_path}


KEY_OCID="ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrlunsfozyf26dg3t2lmoujanqwisyleivxikfsueb5annazwudwtq"
KEY_OCID="ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljr4zczbgi4rskp23hmp5mcb3bp5knbl5yvzsy3rz6idiaiv7isdfoa"

### RSA OAEP without a temporary AES key
ENCRYPTION_ALGORITHM="RSA_OAEP_SHA256"

VAULT_CRYPTO_ENDPOINT="https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com"
PUBLIC_KEY_STRING="`cat ${public_key_path}`"

PRIVATE_KEY_PATH=${private_key_path} # The location of the private key.

SOFTWARE_KEY_PATH="aeskey" # The location for outputting the software-protected master encryption key.
WRAPPED_SOFTWARE_KEY_PATH="wrappedkey"

VAULT_CRYPTO_ENDPOINT="https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com"

# oci kms crypto key export --key-id ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}" --endpoint ${VAULT_CRYPTO_ENDPOINT} 

# wrapped_data=$(oci kms crypto key export --key-id ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}" --endpoint ${VAULT_CRYPTO_ENDPOINT} | grep  encrypted-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')
wrapped_data=$(oci kms crypto key export --key-id ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "`cat ${public_key_path}`" --endpoint ${VAULT_CRYPTO_ENDPOINT} | grep  encrypted-key | cut -d: -f2  | sed 's# "\(.*\)",#\1#g')

# echo ${wrapped_data} >  ${WRAPPED_SOFTWARE_KEY_PATH}.b64
echo ${wrapped_data} | base64 -d > ${WRAPPED_SOFTWARE_KEY_PATH}

# Unwrap the wrapped software-protected key material by using the private RSA wrapping key.
${OPENSSL} pkeyutl -decrypt -in ${WRAPPED_SOFTWARE_KEY_PATH} -inkey ${PRIVATE_KEY_PATH} -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -pkeyopt rsa_mgf1_md:sha256 -out ${SOFTWARE_KEY_PATH}
```
