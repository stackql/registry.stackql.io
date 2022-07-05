---
title: identity_aware_proxy_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_aware_proxy_clients
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
<tr><td><b>Name</b></td><td><code>identity_aware_proxy_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.identity_aware_proxy_clients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Unique identifier of the OAuth client. |
| `displayName` | `string` | Human-friendly name given to the OAuth client. |
| `secret` | `string` | Output only. Client secret of the OAuth client. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_brands_identityAwareProxyClients_get` | `SELECT` | `name` | Retrieves an Identity Aware Proxy (IAP) OAuth client. Requires that the client is owned by IAP. |
| `projects_brands_identityAwareProxyClients_list` | `SELECT` | `parent` | Lists the existing clients for the brand. |
| `projects_brands_identityAwareProxyClients_create` | `INSERT` | `parent` | Creates an Identity Aware Proxy (IAP) OAuth client. The client is owned by IAP. Requires that the brand for the project exists and that it is set for internal-only use. |
| `projects_brands_identityAwareProxyClients_delete` | `DELETE` | `name` | Deletes an Identity Aware Proxy (IAP) OAuth client. Useful for removing obsolete clients, managing the number of clients in a given project, and cleaning up after tests. Requires that the client is owned by IAP. |
| `projects_brands_identityAwareProxyClients_resetSecret` | `EXEC` | `name` | Resets an Identity Aware Proxy (IAP) OAuth client secret. Useful if the secret was compromised. Requires that the client is owned by IAP. |
