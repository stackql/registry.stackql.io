---
title: relyingparty_project_config
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_project_config
  - identitytoolkit
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_project_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty_project_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enableAnonymousUser` | `boolean` | Whether anonymous user is enabled. |
| `allowPasswordUser` | `boolean` | Whether to allow password user sign in or sign up. |
| `useEmailSending` | `boolean` | Whether to use email sending provided by Firebear. |
| `projectId` | `string` | Project ID of the relying party. |
| `idpConfig` | `array` | OAuth2 provider configuration. |
| `legacyResetPasswordTemplate` | `object` | Template for an email template. |
| `apiKey` | `string` | Browser API key, needed when making http request to Apiary. |
| `changeEmailTemplate` | `object` | Template for an email template. |
| `authorizedDomains` | `array` | Authorized domains. |
| `verifyEmailTemplate` | `object` | Template for an email template. |
| `resetPasswordTemplate` | `object` | Template for an email template. |
| `dynamicLinksDomain` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `relyingparty_getProjectConfig` | `SELECT` |  |
