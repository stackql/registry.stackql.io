---
title: memberships
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
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.memberships</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `url` | `string` |  |
| `user` | `object` | Simple User |
| `organization` | `object` | Organization Simple |
| `organization_url` | `string` |  |
| `permissions` | `object` |  |
| `role` | `string` | The user's membership type in the organization. |
| `state` | `string` | The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation. |
## Methods
