---
title: apps
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
<tr><td><b>Name</b></td><td><code>okta.group.apps</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.apps</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `visibility` | `object` |  |
| `profile` | `object` |  |
| `_embedded` | `object` |  |
| `credentials` | `object` |  |
| `status` | `string` |  |
| `signOnMode` | `string` |  |
| `settings` | `object` |  |
| `licensing` | `object` |  |
| `lastUpdated` | `string` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `accessibility` | `object` |  |
| `features` | `array` |  |
| `label` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `groupId` | Enumerates all applications that are assigned to a group. | SELECT |
