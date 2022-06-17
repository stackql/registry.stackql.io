---
title: catalog
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
<tr><td><b>Name</b></td><td><code>catalog</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.userfactor.catalog</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `_links` | `object` |
| `factorType` | `string` |
| `created` | `string` |
| `_embedded` | `object` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `verify` | `object` |
| `provider` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `userId` |
