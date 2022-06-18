---
title: tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `name` | `string` |
| `commit` | `object` |
| `node_id` | `string` |
| `tarball_url` | `string` |
| `zipball_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_tags` | `SELECT` | `owner, repo` |
