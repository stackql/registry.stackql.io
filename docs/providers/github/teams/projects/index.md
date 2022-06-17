---
title: projects
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.projects</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `private` | `boolean` | Whether the project is private or not. Only present when owner is an organization. |
| `columns_url` | `string` |  |
| `number` | `integer` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `owner_url` | `string` |  |
| `body` | `string` |  |
| `organization_permission` | `string` | The organization permission for this project. Only present when owner is an organization. |
| `state` | `string` |  |
| `creator` | `object` | Simple User |
| `node_id` | `string` |  |
| `permissions` | `object` |  |
## Methods
