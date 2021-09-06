## IMP / EXP encryped with my own keypair

### ENV

```bash
OPENSSL="/home/opc/local/bin/openssl.sh"
AES_KEY="aeskey"
WRAPPING_KEY="wrappingkey"
WRAPPED_KEY="wrappedkey"
VAULT_KEYMANAGEMENT_ENDPOINT="https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com"
COMPARTMENT_ID="ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa"
DISPLAY_NAME="mek_keypair2"
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
private_key_path=private.pem
public_key_path=public.pem
rsa_key_size=4096

${OPENSSL_PATH} genrsa -out ${private_key_path} ${rsa_key_size}
${OPENSSL_PATH} rsa -in ${private_key_path} -outform PEM -pubout -out ${public_key_path}

rm wrappingkey
ln -s public.pem wrappingkey

#
# Generate an AES key.
#

${OPENSSL} rand ${KEY_SIZE} > ${AES_KEY}


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
{ "wrappingAlgorithm": "RSA_OAEP_SHA256", "keyMaterial": "JwgqeoEDlE6kBSIWQJbTStGsrQbEm5hyRdn2UvJrkDkh+Mq5QszTJaQSlunBeJZLqvWc66Q3Ei5KXBUF1xA3yGSoe6d6859eKtgJGAPl09ImLyZ3DWd1LFB+PJQG8kZD2Fun7xJltgPo9fWL7V43vwjucB6jOwkB02kl7tN5Ii++0obNxqNVbS8hvQ/1lkcQShyItsNjBBdsp4e3xBtUVgmO17f2hes9nIwTNq1yXNs0hrSPTT7IMEjEiD/9nebDPhSn16l+u3XcRf8SyLnHznIluP/6pjjq8V9oYJoNCjUcC1xbfFIRMIfF4Z57JytyNS8uxOxlBedaMEgYFIJw0Tk6TxRS1LAatNES54bFspCdvRLgwl4ET6CQ2BRe03Yi4uXTjPPJ8XnUQt8ShDU93z1r9MYBbE5rycACb3H5fsqnwjNCwP8y+K6OQlPjXdoNe3wz0+HD798ctbDf3mMkqi/HWdqoPtcc5yFqM2HDdcHeONaSm7X0ZoHcyKAYIpgHv01gdzs2eKO3DKexATrtObcFh5XFAIIC3y80L7hSSevZiTnIhsOkImVTf3yobgJhZMH8z65pB0g0kNQNM4vJ2pAtCA1FMNys1eS77E4xmU87G51xrbcVRChSbnNkw6OJ0IlRJ1oCGsX5P+NGCjxwT1FKAayAE6astg8pbS/TBV4=" }
```

* import key
```
oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ${COMPARTMENT_ID} --display-name ${DISPLAY_NAME} --endpoint ${VAULT_KEYMANAGEMENT_ENDPOINT} --key-shape file://./key_shape.json --protection-mode "${PROTECTION_MODE}"
```
### IMP
```
[opc@ctrl imp]$ oci kms management key import --wrapped-import-key file://./wrapped_import_key.json --compartment-id ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc                                                           3ymzmt3mg4jf5dcnuf4qyzrrqa --display-name mek_keypair2 --endpoint https://cnqtaqh2aagiu-management.kms.ap-seoul-1.oraclecloud.com --key-shape file://./key_shape.json --protec                                                           tion-mode SOFTWARE
{
  "data": {
    "compartment-id": "ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa",
    "current-key-version": "ocid1.keyversion.oc1.ap-seoul-1.cnqtaqh2aagiu.dcu6me3afkyaa.abuwgljr2tmnvrxyrijdgvf6okis77nro5ucolsyrqitykpwi2guw5e6kw4a",
    "defined-tags": {},
    "display-name": "mek_keypair2",
    "freeform-tags": {},
    "id": "ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrdtoo5ox7atvhpwmybdcutzc7abi5ui243kfpokinvb7rj6dywa4q",
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
    "time-created": "2021-09-06T11:59:39.413000+00:00",
    "time-of-deletion": null,
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrktxtvdrfpyykgc4cy7bbtavmaive2poxvucf6bje5hbuyxhtjmoq"
  },
  "etag": "d80562c2ef729bc4c65e63c95c52cdf973b3d5bf"
}

```

## Export Key

### Env

* key_ocid : ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrdtoo5ox7atvhpwmybdcutzc7abi5ui243kfpokinvb7rj6dywa4q

```
KEY_OCID="ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrdtoo5ox7atvhpwmybdcutzc7abi5ui243kfpokinvb7rj6dywa4q"
ENCRYPTION_ALGORITHM="RSA_OAEP_AES_SHA256"
VAULT_CRYPTO_ENDPOINT="https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com"

PUBLIC_KEY_STRING="`cat  wrappingkey.imsi`"
PRIVATE_KEY_PATH="../imp/private_key.pem" # The location of the private key.


SOFTWARE_KEY_PATH="mek" # The location for outputting the software-protected master encryption key.
TEMP_AES_KEY_PATH="tempAes" # The location for outputting the temporary AES key.
TEMP_WRAPPED_AES_PATH="tempWrappedAES" # The location for outputting the wrapped temporary AES key.
WRAPPED_SOFTWARE_KEY_PATH="WrappedMEK"

VAULT_CRYPTO_ENDPOINT="https://cnqtaqh2aagiu-crypto.kms.ap-seoul-1.oraclecloud.com"
OPENSSL="/home/opc/local/bin/openssl.sh"

```
* note : public key 는 new line 없이 문자열로

### Exp

'''
oci kms crypto key export --key-id ${KEY_OCID} --algorithm ${ENCRYPTION_ALGORITHM} --public-key "${PUBLIC_KEY_STRING}" --endpoint ${VAULT_CRYPTO_ENDPOINT}
{
  "data": {
    "algorithm": "RSA_OAEP_AES_SHA256",
    "encrypted-key": "Q92EqKeaTegA8NSC29eT+Z9yJb0UfuUoJo1O3VIObdGyMeRolg7LAHKnV7kEDZV2ZX5TF/QVNsT4ptmgf769E91GQKwdhwzIyKfsv5DrfsfZHvv1ohhKZVM12BIyfNUWAOkMENCX17PsAqWjhWcivTvbfzM1M9BdWo0oBEVOA4wbLAdGNV709VP5c4kEaGJ6gFCyIBUJ4tamEeUAa8mBXixpogI+WyMPsEYZi57FOrJ/O/CHo9ygME/sD3MbrRCKhz0Ta6zs4emTZi9X2nw+DvKHfZQlrK+w733Xj0HknGRcSGhYOWkaBhk/CtuoW7gSAanfanUa6kqrdqP76gY6aGf0T7ky8MrH4UreG3xvB1MZ7LnqiAEsDaRn79RQpnfPGQHv4gD8iGpfd6jNRhgdQMJi5M82i3ByyjPGUrfR2hqLnnbVOly/DzCAh/7PLRpFyBYRr8FFpD14aKdk5uif4LOyNRL7xYi5gsNk98jO4tonHCaeAzHOGeexa9KdpWErKnzpJ41kvDftShij5FI6MdPu8Ys+gJVP2qbNWtI+z4DTTn+b92W7nltcSHs2tseqKCVaZXF02BxgG+0YaKDVpk4Xiz0aNOa+IcWskztY/++G58OVmKtYIhLGv8C5RwhfKnv77Ojgq2v0CWAkQuEhaOaZsnp6gntm57HGZX/Y6zfHgkFNQEQqaDWU/olgKyDkUhQONRq7EmTksCfS44TO0eINLSY5rggn",
    "key-id": "ocid1.key.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljr3qtd6kuq57uan4d6eq3gddnn6swdocydr6igzibylndjowt5juoa",
    "key-version-id": "ocid1.keyversion.oc1.ap-seoul-1.cnqtaqh2aagiu.dcqsme27ehiaa.abuwgljri7ohorxakeyawnjfhffpqj7wd2wwkhve5pcn5dhys4tobhm2g4wq",
    "time-created": "2021-09-06T10:49:01.794000+00:00",
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqtaqh2aagiu.abuwgljrktxtvdrfpyykgc4cy7bbtavmaive2poxvucf6bje5hbuyxhtjmoq"
  }
}
```


```
# Unwrap the wrapped software-protected key material by using the private RSA wrapping key.
 ${OPENSSL} pkeyutl -decrypt -in ${WRAPPED_SOFTWARE_KEY_PATH} -inkey ${PRIVATE_KEY_PATH} -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 -pkeyopt rsa_mgf1_md:sha256 -out ${SOFTWARE_KEY_PATH}
Public Key operation error
140283134453568:error:0406506C:rsa routines:rsa_ossl_private_decrypt:data greater than mod len:crypto/rsa/rsa_ossl.c:401:
```
