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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.group.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `_links` | `object` |
| `settings` | `object` |
| `_embedded` | `object` |
| `created` | `string` |
| `licensing` | `object` |
| `accessibility` | `object` |
| `label` | `string` |
| `lastUpdated` | `string` |
| `profile` | `object` |
| `status` | `string` |
| `signOnMode` | `string` |
| `features` | `array` |
| `credentials` | `object` |
| `visibility` | `object` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `groupId` |