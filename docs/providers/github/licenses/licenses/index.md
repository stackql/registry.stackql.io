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
<tr><td><b>Id</b></td><td><code>github.licenses.licenses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `name` | `string` |
| `description` | `string` |
| `url` | `string` |
| `node_id` | `string` |
| `body` | `string` |
| `featured` | `boolean` |
| `conditions` | `array` |
| `implementation` | `string` |
| `spdx_id` | `string` |
| `html_url` | `string` |
| `key` | `string` |
| `limitations` | `array` |
| `permissions` | `array` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `license` |
