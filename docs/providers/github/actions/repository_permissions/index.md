---
title: repository_permissions
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
<tr><td><b>Name</b></td><td><code>repository_permissions</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repository_permissions</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `enabled` | `boolean` | Whether GitHub Actions is enabled on the repository. |
| `selected_actions_url` | `string` | The API URL to use to get or set the actions that are allowed to run, when `allowed_actions` is set to `selected`. |
| `allowed_actions` | `string` | The permissions policy that controls the actions that are allowed to run. Can be one of: `all`, `local_only`, or `selected`. |
## Methods
