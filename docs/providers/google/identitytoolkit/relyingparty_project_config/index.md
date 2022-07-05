---
title: relyingparty_project_config
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_project_config
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
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
| `dynamicLinksDomain` | `string` |  |
| `enableAnonymousUser` | `boolean` | Whether anonymous user is enabled. |
| `resetPasswordTemplate` | `object` | Template for an email template. |
| `useEmailSending` | `boolean` | Whether to use email sending provided by Firebear. |
| `verifyEmailTemplate` | `object` | Template for an email template. |
| `idpConfig` | `array` | OAuth2 provider configuration. |
| `changeEmailTemplate` | `object` | Template for an email template. |
| `legacyResetPasswordTemplate` | `object` | Template for an email template. |
| `projectId` | `string` | Project ID of the relying party. |
| `apiKey` | `string` | Browser API key, needed when making http request to Apiary. |
| `authorizedDomains` | `array` | Authorized domains. |
| `allowPasswordUser` | `boolean` | Whether to allow password user sign in or sign up. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `relyingparty_getProjectConfig` | `SELECT` |  |
