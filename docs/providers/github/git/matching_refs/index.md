---
title: matching_refs
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
<tr><td><b>Name</b></td><td><code>matching_refs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.git.matching_refs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `ref` | `string` |
| `url` | `string` |
| `node_id` | `string` |
| `object` | `object` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_matching_refs` | `SELECT` | `owner, ref, repo` |
