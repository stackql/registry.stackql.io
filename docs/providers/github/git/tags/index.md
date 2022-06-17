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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.git.tags</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `verification` | `object` |  |
| `message` | `string` | Message describing the purpose of the tag |
| `node_id` | `string` |  |
| `object` | `object` |  |
| `sha` | `string` |  |
| `tag` | `string` | Name of the tag |
| `tagger` | `object` |  |
| `url` | `string` | URL for the tag |
## Methods
