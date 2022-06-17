---
title: self_hosted_runner_groups
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_groups</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runner_groups</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `number` |  |
| `name` | `string` |  |
| `inherited` | `boolean` |  |
| `runners_url` | `string` |  |
| `visibility` | `string` |  |
| `selected_repositories_url` | `string` | Link to the selected repositories resource for this runner group. Not present unless visibility was set to `selected` |
| `allows_public_repositories` | `boolean` |  |
| `inherited_allows_public_repositories` | `boolean` |  |
| `default` | `boolean` |  |
## Methods
