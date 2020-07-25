## Ansbile
### Cloud modules
* https://oracle-cloud-infrastructure-ansible-modules.readthedocs.io/en/latest/modules/list_of_cloud_modules.html
### Document
* [Getting Started with Ansible](https://docs.ansible.com/ansible/devel/user_guide/intro_getting_started.html)
* [Getting Started with Ansible for OCI](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansiblegetstarted.htm)
* [Cloud Modules for OCI](https://oracle-cloud-infrastructure-ansible-modules.readthedocs.io/en/latest/modules/list_of_cloud_modules.html)
* [OCI Ansible Modules Github Repo](https://github.com/oracle/oci-ansible-modules)
### Setup
* Oracle Cloud Infrastructure Ansible Modules can also be downloaded from Ansible Galaxy and used as roles.
```bash
$ sudo yum install ansible
$ ansible-galaxy install oracle.oci_ansible_modules
$ pip install oci
```
### Examples
#### [``OCI Ansible Modules Github repository``](https://github.com/oracle/oci-ansible-modules)
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
### Sample 
* env
```bash
[opc@ctrl ansible]$ cat env_vars
# OCID of assigned compartment
export compartment_ocid=ocid1.compartment.oc1..aaaaaaaabsnkmaevlvzry2bigiv6eumncc3ymzmt3mg4jf5dcnuf4qyzrrqa
export namespace_name=cnuyg9lmqgql

# Oracle-Linux-7.7-2019.08-28-0
#Seoul
export image_ocid=ocid1.image.oc1.ap-seoul-1.aaaaaaaautl44ij44xudvnu3boasvuvucowuz4avdigc2csahzqmtb37sfwa
# skip host verification prompts for demo
export ANSIBLE_HOST_KEY_CHECKING=False
```
* simple examples : ex.yaml
```bash
[opc@ctrl ansible]$ cat ex.yaml
- hosts: localhost
  roles:
    - { role: oracle.oci_ansible_modules }
  vars:
    compartment_id: "{{ lookup('env', 'compartment_ocid') }}"
    namespace_name: "{{ lookup('env', 'namespace_name') }}"
  tasks:
    - name: Get all the buckets in the namespace
      oci_bucket_facts:
        namespace_name: "{{ namespace_name }}"
        compartment_id: "{{ compartment_id }}"

```
* run playbook
```bash
[opc@ctrl ansible]$ ansible-playbook ex.yaml
 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] *****************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************
ok: [localhost]

TASK [Get all the buckets in the namespace] **************************************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "oci python sdk required for this module"}

PLAY RECAP ***********************************************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0


```
