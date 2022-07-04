---
title: service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - service_accounts
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
<tr><td><b>Name</b></td><td><code>service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iamcredentials.service_accounts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_serviceAccounts_generateAccessToken` | `EXEC` | `name` | Generates an OAuth 2.0 access token for a service account. |
| `projects_serviceAccounts_generateIdToken` | `EXEC` | `name` | Generates an OpenID Connect ID token for a service account. |
| `projects_serviceAccounts_signBlob` | `EXEC` | `name` | Signs a blob using a service account's system-managed private key. |
| `projects_serviceAccounts_signJwt` | `EXEC` | `name` | Signs a JWT using a service account's system-managed private key. |