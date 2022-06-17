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
<tr><td><b>Id</b></td><td><code>github.projects.projects</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` | Name of the project |
| `created_at` | `string` |  |
| `body` | `string` | Body of the project |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `number` | `integer` |  |
| `html_url` | `string` |  |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `columns_url` | `string` |  |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `node_id` | `string` |  |
| `owner_url` | `string` |  |
| `creator` | `object` | Simple User |
| `url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
