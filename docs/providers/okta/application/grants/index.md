---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>okta.application.grants</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.grants</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `_links` | `object` |  |
| `source` | `string` |  |
| `createdBy` | `object` |  |
| `created` | `string` |  |
| `lastUpdated` | `string` |  |
| `scopeId` | `string` |  |
| `issuer` | `string` |  |
| `status` | `string` |  |
| `clientId` | `string` |  |
| `_embedded` | `object` |  |
| `userId` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `appId, grantId` | Fetches a single scope consent grant for the application | SELECT |
| `list` | `appId` | Lists all scope consent grants for the application | SELECT |
| `insert` | `appId` | Grants consent for the application to request an OAuth 2.0 Okta scope | INSERT |
| `delete` | `appId, grantId` | Revokes permission for the application to request the given scope | DELETE |
