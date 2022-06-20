---
title: management.accountUserLinks
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
<tr><td><b>Name</b></td><td><code>management.accountUserLinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.accountUserLinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Entity user link ID |
| `permissions` | `object` | Permissions the user has for this entity. |
| `selfLink` | `string` | Self link for this resource. |
| `userRef` | `object` | JSON template for a user reference. |
| `entity` | `object` | Entity for this link. It can be an account, a web property, or a view (profile). |
| `kind` | `string` | Resource type for entity user link. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `accountId` | Lists account-user links for a given account. |
| `insert` | `INSERT` | `accountId` | Adds a new user to the given account. |
| `delete` | `DELETE` | `accountId, linkId` | Removes a user from the given account. |
| `update` | `EXEC` | `accountId, linkId` | Updates permissions for an existing user on the given account. |
