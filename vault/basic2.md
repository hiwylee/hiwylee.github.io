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
