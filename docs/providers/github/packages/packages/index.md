---
title: packages
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
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.packages.packages</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the package. |
| `name` | `string` | The name of the package. |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `package_type` | `string` |  |
| `owner` | `object` | Simple User |
| `updated_at` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `version_count` | `integer` | The number of versions of the package. |
| `visibility` | `string` |  |
## Methods
