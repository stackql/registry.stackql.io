---
title: artifacts
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.artifacts</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` | The name of the artifact. |
| `archive_download_url` | `string` |  |
| `expires_at` | `string` |  |
| `url` | `string` |  |
| `size_in_bytes` | `integer` | The size in bytes of the artifact. |
| `expired` | `boolean` | Whether or not the artifact has expired. |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
