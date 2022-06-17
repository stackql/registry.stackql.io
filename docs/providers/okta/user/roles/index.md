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
<tr><td><b>Name</b></td><td><code>okta.user.roles</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.roles</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `_embedded` | `object` |  |
| `label` | `string` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `type` | `string` |  |
| `assignmentType` | `string` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `roleId, userId` | Gets role that is assigne to user. | SELECT |
| `list` | `userId` | Lists all roles assigned to a user. | SELECT |
| `insert` | `userId` | Assigns a role to a user. | INSERT |
| `delete` | `roleId, userId` | Unassigns a role from a user. | DELETE |
