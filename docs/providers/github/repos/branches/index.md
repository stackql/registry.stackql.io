---
title: branches
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
<tr><td><b>Name</b></td><td><code>branches</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.branches</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `protection_url` | `string` |  |
| `required_approving_review_count` | `integer` |  |
| `_links` | `object` |  |
| `commit` | `object` | Commit |
| `pattern` | `string` |  |
| `protected` | `boolean` |  |
| `protection` | `object` | Branch Protection |
## Methods
