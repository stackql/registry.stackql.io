---
title: release_assets
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
<tr><td><b>Name</b></td><td><code>release_assets</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.release_assets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` | The file name of the asset. |
| `download_count` | `integer` |  |
| `uploader` | `object` | Simple User |
| `updated_at` | `string` |  |
| `state` | `string` | State of the release asset. |
| `label` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `content_type` | `string` |  |
| `url` | `string` |  |
| `browser_download_url` | `string` |  |
| `size` | `integer` |  |
## Methods
