---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `status` | `string` |
| `passwordChanged` | `string` |
| `profile` | `object` |
| `activated` | `string` |
| `lastLogin` | `string` |
| `created` | `string` |
| `credentials` | `object` |
| `_embedded` | `object` |
| `transitioningToStatus` | `string` |
| `lastUpdated` | `string` |
| `_links` | `object` |
| `statusChanged` | `string` |
| `type` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `groupId` | Enumerates all users that are a member of a group. |
| `insert` | `INSERT` | `groupId, userId` | Adds a user to a group with 'OKTA_GROUP' type. |
| `delete` | `DELETE` | `groupId, userId` | Removes a user from a group with 'OKTA_GROUP' type. |