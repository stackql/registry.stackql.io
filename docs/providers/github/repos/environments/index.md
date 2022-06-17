---
title: environments
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.environments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The id of the environment. |
| `name` | `string` | The name of the environment. |
| `deployment_branch_policy` | `object` | The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`. |
| `updated_at` | `string` | The time that the environment was last updated, in ISO 8601 format. |
| `node_id` | `string` |  |
| `protection_rules` | `array` |  |
| `url` | `string` |  |
| `created_at` | `string` | The time that the environment was created, in ISO 8601 format. |
| `html_url` | `string` |  |
## Methods
