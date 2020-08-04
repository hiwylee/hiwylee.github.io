## Oracle Identity Cloud Service
### Tutorials
* https://docs.oracle.com/en/cloud/paas/identity-cloud/tutorials.html
* Use OAuth 2.0 and Open ID Connect in a Custom Application
  * https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:13427
## Federating with Identity Providers [link](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm)
### [Federating with SAML 2.0 Identity Providers](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
* [Oracle Cloud Infrastructure Okta Configuration for Federation and Provisioning](https://cloud.oracle.com/iaas/whitepapers/okta-federation-with-oci.pdf)
* [Federating Oracle Access Manager to Oracle Cloud Infrastructure](https://cloud.oracle.com/iaas/whitepapers/oracle_access_manager_federation_to_oci.pdf)
### Instructions for Federating
#### [Federating with SAML 2.0 Identity Providers](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top)
* Before following the steps in this topic, see [Federating with Identity Providers](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top) to ensure that you understand general federation concepts.
#### [설정 순서](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm#top)
> [``문서참조``](https://docs.cloud.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm#top)
<!--
> In the Oracle Cloud Infrastructure Console, 
1. get the federation metadata required to establish a trust relationship with the Identity Provider (IdP).
> In the IdP
2. Configure Oracle Cloud Infrastructure as an application (sometimes called a trusted relying party).
3. Assign users and groups to your new Oracle Cloud Infrastructure application.
4. Get the required information needed by Oracle Cloud Infrastructure.
> In Oracle Cloud Infrastructure:
5. Add the identity provider to your tenancy and provide information you got from the IdP.
6. Map the IdP's groups to IAM groups.
7. Make sure you have IAM policies set up for the groups so you can control users' access to Oracle Cloud Infrastructure resources.
8. Inform your users of the name of your Oracle Cloud Infrastructure tenant and the URL for the Console (for example, https://console.us-ashburn-1.oraclecloud.com).
-->
* Step 1: Get information from Oracle Cloud Infrastructure
* Step 2: Set up Oracle Cloud Infrastructure as a trusted application
* Step 3: Assign users and groups to the new application.
* Step 4: Download the IdP's metadata document.
* Step 5: Federate the IdP with Oracle Cloud Infrastructure
* Step 6: Set up IAM policies for the groups
* Step 7: Give your federated users the name of the tenant and URL to sign in
