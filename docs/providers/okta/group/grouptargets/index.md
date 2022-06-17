---
title: grouptargets
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
<tr><td><b>Name</b></td><td><code>okta.group.grouptargets</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.grouptargets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `_embedded` | `object` |  |
| `lastUpdated` | `string` |  |
| `objectClass` | `array` |  |
| `lastMembershipUpdated` | `string` |  |
| `profile` | `object` |  |
| `created` | `string` |  |
| `type` | `string` |  |
| `_links` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `groupId, roleId` | Success | SELECT |
| `insert` | `groupId, roleId, targetGroupId` |  | INSERT |
| `delete` | `groupId, roleId, targetGroupId` |  | DELETE |