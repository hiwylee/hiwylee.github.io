## Basic Test
* vault ocid : ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq

### Endpoint
* Vault Service Key Management API: https://kms.ap-seoul-1.oraclecloud.com
* Vault Service Secret Management API : https://vaults.ap-seoul-1.oci.oraclecloud.com/20180608
* Vault Service Secret Retrieval API  : https://secrets.vaults.ap-seoul-1.oci.oraclecloud.com/20190301
### list vault

```
wonyong_le@cloudshell:~ (ap-seoul-1)$ oci kms management vault get --vault-id ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq
{
  "data": {
    "compartment-id": "ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla",
    "crypto-endpoint": "https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com",
    "defined-tags": {
      "Global-Tags": {
        "CreatedBy": "oracleidentitycloudservice/wonyong.lee@oracle.com",
        "CreatedOn": "2021-08-13T17:19:58.882Z"
      }
    },
    "display-name": "tde_key",
    "freeform-tags": {},
    "id": "ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq",
    "is-primary": true,
    "lifecycle-state": "ACTIVE",
    "management-endpoint": "https://cnqrnkn6aagiu-management.kms.ap-seoul-1.oraclecloud.com",
    "replica-details": null,
    "restored-from-vault-id": null,
    "time-created": "2021-08-13T17:19:59.284000+00:00",
    "time-of-deletion": null,
    "vault-type": "DEFAULT",
    "wrappingkey-id": "ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrztel222tg4bucstdqmqwtbaz2z26exikenaz5skbh2szzdk7mw2q"
  },
  "etag": "6e6660a297a99fd65c80750715b2d6a6fd537107--gzip"
}
```

```

wonyong_le@cloudshell:.oci (ap-seoul-1)$ oci kms management vault list --compartment-id $C --all
{
  "data": [
    {
      "compartment-id": "ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla",
      "crypto-endpoint": "https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com",
      "defined-tags": {
        "Global-Tags": {
          "CreatedBy": "oracleidentitycloudservice/wonyong.lee@oracle.com",
          "CreatedOn": "2021-08-13T17:19:58.882Z"
        }
      },
      "display-name": "tde_key",
      "freeform-tags": {},
      "id": "ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq",
      "lifecycle-state": "ACTIVE",
      "management-endpoint": "https://cnqrnkn6aagiu-management.kms.ap-seoul-1.oraclecloud.com",
      "time-created": "2021-08-13T17:19:59.284000+00:00",
      "vault-type": "DEFAULT"
    }
  ]
}

wonyong_le@cloudshell:.oci (ap-seoul-1)$ oci kms management wrapping-key get --endpoint https://cnqrnkn6aagiu-management.kms.ap-seoul-1.oraclecloud.com
{
  "data": {
    "compartment-id": "ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla",
    "id": "ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrztel222tg4bucstdqmqwtbaz2z26exikenaz5skbh2szzdk7mw2q",
    "lifecycle-state": "ENABLED",
    "public-key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA0h5wAcDA90Jm9CdP4sVv\r\nF4HuqTiPaHiRELosDBEX/Ab22EZ6BbYnzcf365Ahm2UJARPp7dNblhV3yIf6NR+R\r\ntOLGXsCIiLbefI9xmb60LGLATEMhhpmFfGJndKTWIJg0zui9Uui8IqhnwS5VIzEW\r\n2C41XO0yxF+qwVFtvEaxiD72H6L+GDUUkF0cOyU4QXYj5rp44DTs9bNF+9jFbQgY\r\nHDUNgKv5b41lTDGiz1ZzBGtM5/JWeUTYgX5QQJAqsy9dHDrmen3Wy7+lysrCbnIw\r\nHxXLdmHLy02ifV74QY6VFbBLPNZqDrgqgMxNOk4cs+9O1QmopUQEnTrUteIXhAra\r\n4QItySrwjMuU7TEEXUXBjItD++ZmsTjs56UPST3ZqRBSfB/w+iMz7PrhZpWc1J7F\r\nW8Q7nQH1iMlL5lsEHRIki9eEisIx5HOGFuXXJmO9wJMTgsmEzil0+F7bBCp5GXvf\r\n73BPIHkAS3HqAM80VDCeRfc/Oc55xVLPN80VVHnWqs+kYDkXAEMtIcNI8uy+Ix/V\r\nPJ3cRolIcX7NrZHrVAoOhtwWyW/VI6vkZPr0cJKZApcJ8alWnpvOZGTorzsdl5fE\r\nkWzXvZeG/Rj1Z4bjHzZMChh4HZE5etpvS+oTREJZ0aZDOTuQ9plnhwaOnbd10Qx/\r\nLODKvKxMKvIJ3NVW2sogcMsCAwEAAQ==\r\n-----END PUBLIC KEY-----\n",
    "time-created": "2021-08-13T17:20:08.051000+00:00",
    "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq"
  },
  "etag": "ff50f0e4e088895553cd601585857be5846eb33f--gzip"
}


wonyong_le@cloudshell:.oci (ap-seoul-1)$ oci kms management key list  --compartment-id $C  --endpoint https://cnqrnkn6aagiu-management.kms.ap-seoul-1.oraclecloud.com --all
{
  "data": [
    {
      "algorithm": "AES",
      "compartment-id": "ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla",
      "defined-tags": {},
      "display-name": "tde_key",
      "freeform-tags": {},
      "id": "ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq",
      "lifecycle-state": "ENABLED",
      "protection-mode": "SOFTWARE",
      "time-created": "2021-08-13T17:44:09.660000+00:00",
      "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq"
    }
  ]
}

oci kms crypto  encrypt --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq --plaintext "HELLO" --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com

oci kms crypto  encrypt --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq --plaintext "HELLO" --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com


 export compartment_id=ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/create.html#cmdoption-compartment-id
 export display_name="ENCRYPT KEY" # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/create.html#cmdoption-display-name
 export plaintext="HELLO" # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/crypto/encrypt.html#cmdoption-plaintext

    key_id=$(oci kms management key create --compartment-id $compartment_id --display-name $display_name --endpoint https://region.domain.com --key-shape file://key-shape.json --query data.id --raw-output)

    oci kms crypto encrypt --endpoint https://region.domain.com --key-id $key_id --plaintext $plaintext
	
wonyong_le@cloudshell:.oci (ap-seoul-1)$ oci kms management key list  --compartment-id $C  --endpoint https://cnqrnkn6aagiu-management.kms.ap-seoul-1.oraclecloud.com --all{
  "data": [
    {
      "algorithm": "AES",
      "compartment-id": "ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla",
      "defined-tags": {},
      "display-name": "enc_key",
      "freeform-tags": {},
      "id": "ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrbidjrsio4mpprxio3aoussswmshkvyegvwrpzkgq6m6nrolbkoqa",
      "lifecycle-state": "CREATING",
      "protection-mode": "HSM",
      "time-created": "2021-09-01T12:06:39.921000+00:00",
      "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq"
    },
    {
      "algorithm": "AES",
      "compartment-id": "ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla",
      "defined-tags": {},
      "display-name": "tde_key",
      "freeform-tags": {},
      "id": "ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq",
      "lifecycle-state": "ENABLED",
      "protection-mode": "SOFTWARE",
      "time-created": "2021-08-13T17:44:09.660000+00:00",
      "vault-id": "ocid1.vault.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrxywbmswpdbdbilxrnelpi2lokiq44astjshxgiefxu7l2qdg43pq"
    }
  ]
}


oci kms crypto  encrypt --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq --plaintext `echo -n "HELLO WORLD" | base64` --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com

oci kms crypto  encrypt --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrbidjrsio4mpprxio3aoussswmshkvyegvwrpzkgq6m6nrolbkoqa --plaintext `echo -n "HELLO WORLD" | base64` --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com




 oci kms crypto  encrypt --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq --plaintext `echo -n "HELLO WORLD" | base64` --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com
{
  "data": {
    "ciphertext": "QUu67mMnK/g6qGeqbRfR/PEiFXY4RC8OQZFt/CBfpK646w1+gw5lNsvGeTZA1x8o",
    "encryption-algorithm": null,
    "key-id": null,
    "key-version-id": null
  }
}


oci kms crypto decrypt --ciphertext "QUu67mMnK/g6qGeqbRfR/PEiFXY4RC8OQZFt/CBfpK646w1+gw5lNsvGeTZA1x8o" --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrwmtnmwymzu2ikzjp43as3fa66ohcteizofzb5fe36rqpxwsq47vq --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com



{
  "data": {
    "encryption-algorithm": null,
    "key-id": null,
    "key-version-id": null,
    "plaintext": "SEVMTE8gV09STEQ=",
    "plaintext-checksum": "2279966299"
  }
}

 echo "SEVMTE8gV09STEQ=" | base64 --decode
HELLO WORLD


 oci kms crypto  encrypt --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrbidjrsio4mpprxio3aoussswmshkvyegvwrpzkgq6m6nrolbkoqa --plaintext `echo -n "HELLO WORLD" | base64` --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com
{
  "data": {
    "ciphertext": "QcyE8DFeCPeIAIG6tqhKM4/G2DuWwNpg4hz3hMawlJ3VGTDaBVzOrR9wO9BMpyYv+gAAAAA=",
    "encryption-algorithm": null,
    "key-id": null,
    "key-version-id": null
  }
}


oci kms crypto decrypt --ciphertext "QcyE8DFeCPeIAIG6tqhKM4/G2DuWwNpg4hz3hMawlJ3VGTDaBVzOrR9wO9BMpyYv+gAAAAA=" --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrbidjrsio4mpprxio3aoussswmshkvyegvwrpzkgq6m6nrolbkoqa --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com
oci kms crypto decrypt --ciphertext "QcyE8DFeCPeIAIG6tqhKM4/G2DuWwNpg4hz3hMawlJ3VGTDaBVzOrR9wO9BMpyYv+gAAAAA=" --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrbidjrsio4mpprxio3aoussswmshkvyegvwrpzkgq6m6nrolbkoqa --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com
{
  "data": {
    "encryption-algorithm": null,
    "key-id": null,
    "key-version-id": null,
    "plaintext": "SEVMTE8gV09STEQ=",
    "plaintext-checksum": "2279966299"
  }
}

echo "SEVMTE8gV09STEQ=" | base64 --decode
HELLO WORLD

oci kms crypto decrypt --ciphertext "QcyE8DFeCPeIAIG6tqhKM4/G2DuWwNpg4hz3hMawlJ3VGTDaBVzOrR9wO9BMpyYv+gAAAAA=" --key-id ocid1.key.oc1.ap-seoul-1.cnqrnkn6aagiu.abuwgljrbidjrsio4mpprxio3aoussswmshkvyegvwrpzkgq6m6nrolbkoqa --endpoint https://cnqrnkn6aagiu-crypto.kms.ap-seoul-1.oraclecloud.com --query data.plaintext 
"SEVMTE8gV09STEQ="

```
