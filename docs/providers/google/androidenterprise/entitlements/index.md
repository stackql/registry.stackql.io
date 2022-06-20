---
title: entitlements
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
<tr><td><b>Name</b></td><td><code>entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.entitlements</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, entitlementId, userId` | Retrieves details of an entitlement. |
| `list` | `SELECT` | `enterpriseId, userId` | Lists all entitlements for the specified user. Only the ID is set. |
| `delete` | `DELETE` | `enterpriseId, entitlementId, userId` | Removes an entitlement to an app for a user. |
| `update` | `EXEC` | `enterpriseId, entitlementId, userId` | Adds or updates an entitlement to an app for a user. |
