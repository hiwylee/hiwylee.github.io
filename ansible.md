## Ansbile
### Cloud modules
* https://oracle-cloud-infrastructure-ansible-modules.readthedocs.io/en/latest/modules/list_of_cloud_modules.html
### Document
* [Getting Started with Ansible](https://docs.ansible.com/ansible/devel/user_guide/intro_getting_started.html)
* [Getting Started with Ansible for OCI](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansiblegetstarted.htm)
* [Cloud Modules for OCI](https://oracle-cloud-infrastructure-ansible-modules.readthedocs.io/en/latest/modules/list_of_cloud_modules.html)
* [OCI Ansible Modules Github Repo](https://github.com/oracle/oci-ansible-modules)

### Examples
#### OCI Ansible Modules Github repository 
* Create a directory (i.e. ansible-oci) and in that directory a file called env-vars
* insert the following three lines into the env-vars file:
```bash
SAMPLE_COMPARTMENT_OCID=<your compartment OCID>
SAMPLE_IMAGE_OCID=<desired image OCID>
SAMPLE_AD_NAME=<desired AD name>
```
* Give it a try! 
```bash
$ source env-vars
$ git clone https://github.com/oracle/oci-ansible-modules.git 
$ cd oci-ansible-modules/samples/compute/nat-instance-configuration
$ ansible-playbook sample.yaml

```
