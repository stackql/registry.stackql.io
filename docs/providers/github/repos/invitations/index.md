---
title: invitations
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.invitations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository invitation. |
| `created_at` | `string` |  |
| `expired` | `boolean` | Whether or not the invitation has expired |
| `invitee` | `object` | Simple User |
| `node_id` | `string` |  |
| `permissions` | `string` | The permission associated with the invitation. |
| `repository` | `object` | Minimal Repository |
| `url` | `string` | URL for the repository invitation |
| `html_url` | `string` |  |
| `inviter` | `object` | Simple User |
## Methods
