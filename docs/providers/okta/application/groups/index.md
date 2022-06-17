---
title: groups
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `lastUpdated` | `string` |
| `priority` | `integer` |
| `profile` | `object` |
| `_embedded` | `object` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `appId, groupId` | Fetches an application group assignment |
| `list` | `SELECT` | `appId` | Enumerates group assignments for an application. |
| `delete` | `DELETE` | `appId, groupId` | Removes a group assignment from an application. |
| `update` | `EXEC` | `appId, groupId` | Assigns a group to an application |
