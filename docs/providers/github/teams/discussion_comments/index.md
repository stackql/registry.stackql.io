---
title: discussion_comments
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
<tr><td><b>Name</b></td><td><code>discussion_comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.discussion_comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `last_edited_at` | `string` |  |
| `number` | `integer` | The unique sequence number of a team discussion comment. |
| `body_html` | `string` |  |
| `body_version` | `string` | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. |
| `url` | `string` |  |
| `body` | `string` | The main text of the comment. |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `author` | `object` | Simple User |
| `discussion_url` | `string` |  |
| `node_id` | `string` |  |
| `reactions` | `object` |  |
| `updated_at` | `string` |  |
## Methods
