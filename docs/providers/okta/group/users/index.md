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
<tr><td><b>Name</b></td><td><code>okta.group.users</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.users</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `activated` | `string` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
| `passwordChanged` | `string` |  |
| `credentials` | `object` |  |
| `profile` | `object` |  |
| `transitioningToStatus` | `string` |  |
| `type` | `object` |  |
| `statusChanged` | `string` |  |
| `_links` | `object` |  |
| `_embedded` | `object` |  |
| `lastLogin` | `string` |  |
| `created` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `groupId` | Enumerates all users that are a member of a group. | SELECT |
| `insert` | `groupId, userId` | Adds a user to a group with 'OKTA_GROUP' type. | INSERT |
| `delete` | `groupId, userId` | Removes a user from a group with 'OKTA_GROUP' type. | DELETE |