---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.scim.users</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Unique identifier of an external identity |
| `name` | `object` |  |
| `displayName` | `string` | The name of the user, suitable for display to end-users |
| `externalId` | `string` | The ID of the User. |
| `operations` | `array` | Set of operations to be performed |
| `userName` | `string` | Configured by the admin. Could be an email, login, or username |
| `active` | `boolean` | The active status of the User. |
| `meta` | `object` |  |
| `organization_id` | `integer` | The ID of the organization. |
| `emails` | `array` | user emails |
| `groups` | `array` | associated groups |
| `schemas` | `array` | SCIM schema used. |
## Methods
