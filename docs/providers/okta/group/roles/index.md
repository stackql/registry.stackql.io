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
<tr><td><b>Name</b></td><td><code>okta.group.roles</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.roles</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `lastUpdated` | `string` |  |
| `_links` | `object` |  |
| `assignmentType` | `string` |  |
| `status` | `string` |  |
| `created` | `string` |  |
| `label` | `string` |  |
| `type` | `string` |  |
| `_embedded` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `groupId, roleId` | Success | SELECT |
| `list` | `groupId` | Success | SELECT |
| `insert` | `groupId` | Assigns a Role to a Group | INSERT |
| `delete` | `groupId, roleId` | Unassigns a Role from a Group | DELETE |
