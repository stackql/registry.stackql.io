---
title: licenses
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
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.licenses.licenses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `name` | `string` |
| `description` | `string` |
| `permissions` | `array` |
| `key` | `string` |
| `conditions` | `array` |
| `featured` | `boolean` |
| `spdx_id` | `string` |
| `node_id` | `string` |
| `body` | `string` |
| `implementation` | `string` |
| `limitations` | `array` |
| `url` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `license` |
