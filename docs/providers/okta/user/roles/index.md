---
title: roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `description` | `string` |
| `label` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `assignmentType` | `string` |
| `_embedded` | `object` |
| `_links` | `object` |
| `created` | `string` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `roleId, userId` | Gets role that is assigne to user. |
| `list` | `SELECT` | `userId` | Lists all roles assigned to a user. |
| `insert` | `INSERT` | `userId` | Assigns a role to a user. |
| `delete` | `DELETE` | `roleId, userId` | Unassigns a role from a user. |
