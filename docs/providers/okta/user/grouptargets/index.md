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
<tr><td><b>Name</b></td><td><code>grouptargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.grouptargets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `type` | `string` |
| `profile` | `object` |
| `lastMembershipUpdated` | `string` |
| `created` | `string` |
| `_embedded` | `object` |
| `objectClass` | `array` |
| `_links` | `object` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `roleId, userId` |
| `insert` | `INSERT` | `groupId, roleId, userId` |
| `delete` | `DELETE` | `groupId, roleId, userId` |
