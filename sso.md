## Federating with Identity Providers [link](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm)
### [Federating with SAML 2.0 Identity Providers](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
* [Oracle Cloud Infrastructure Okta Configuration for Federation and Provisioning](https://cloud.oracle.com/iaas/whitepapers/okta-federation-with-oci.pdf)
* [Federating Oracle Access Manager to Oracle Cloud Infrastructure](https://cloud.oracle.com/iaas/whitepapers/oracle_access_manager_federation_to_oci.pdf)
### Instructions for Federating
#### [Federating with Identity Providers](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top)
* Before following the steps in this topic, see [Federating with Identity Providers](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top) to ensure that you understand general federation concepts.
#### 설정 순서
1. In the Oracle Cloud Infrastructure Console, get the federation metadata required to establish a trust relationship with the Identity Provider (IdP).
2. In the IdP, configure Oracle Cloud Infrastructure as an application (sometimes called a trusted relying party).
3. In the IdP, assign users and groups to your new Oracle Cloud Infrastructure application.
4. In the IdP, get the required information needed by Oracle Cloud Infrastructure.
5. In Oracle Cloud Infrastructure:
  1. Add the identity provider to your tenancy and provide information you got from the IdP.
  2. Map the IdP's groups to IAM groups.
  3. In Oracle Cloud Infrastructure, make sure you have IAM policies set up for the groups so you can control users' access to Oracle Cloud Infrastructure resources.
  4. Inform your users of the name of your Oracle Cloud Infrastructure tenant and the URL for the Console (for example, https://console.us-ashburn-1.oraclecloud.com).
