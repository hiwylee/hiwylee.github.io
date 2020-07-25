## Terraform
* [Oracle Cloud Infrastructure Provider](https://www.terraform.io/docs/providers/oci/index.html)
* [Oracle Cloud Infrastructure Provider Examples](https://github.com/terraform-providers/terraform-provider-oci/tree/master/examples)

### Deploying Infrastructure Using Terraform
* https://github.com/oracle/learning-library/blob/master/oci-library/qloudable/Infra_Using_Terraform/Infra_Using_Terraform.md
### env_vars
```bash
export TF_VAR_tenancy_ocid="ocid1.tenancy.oc1..xx"
export TF_VAR_user_ocid="ocid1.user.oc1..axx"
export TF_VAR_fingerprint="a0:93:f1:91:53:xx"
export TF_VAR_region="ap-seoul-1"
export TF_VAR_private_key_path=~/.oci/oci_api_key.pem
export TF_VAR_compartment_ocid="ocid1.compartment.oc1..xx"

export TF_VAR_ssh_public_key=$(cat ~/.ssh/id_rsa.pub)
export TF_VAR_ssh_privatek_ey=$(cat ~/.ssh/id_rsa)
```
