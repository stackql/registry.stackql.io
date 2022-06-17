---
title: self_hosted_runners
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
<tr><td><b>Name</b></td><td><code>self_hosted_runners</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runners</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The id of the runner. |
| `name` | `string` | The name of the runner. |
| `busy` | `boolean` |  |
| `labels` | `array` |  |
| `os` | `string` | The Operating System of the runner. |
| `status` | `string` | The status of the runner. |
## Methods
