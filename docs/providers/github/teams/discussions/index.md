---
title: discussions
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
<tr><td><b>Name</b></td><td><code>discussions</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.discussions</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `reactions` | `object` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
| `last_edited_at` | `string` |  |
| `updated_at` | `string` |  |
| `number` | `integer` | The unique sequence number of a team discussion. |
| `comments_count` | `integer` |  |
| `body_html` | `string` |  |
| `team_url` | `string` |  |
| `created_at` | `string` |  |
| `author` | `object` | Simple User |
| `comments_url` | `string` |  |
| `body` | `string` | The main text of the discussion. |
| `private` | `boolean` | Whether or not this discussion should be restricted to team members and organization administrators. |
| `node_id` | `string` |  |
| `pinned` | `boolean` | Whether or not this discussion should be pinned for easy retrieval. |
| `body_version` | `string` | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. |
| `title` | `string` | The title of the discussion. |
## Methods
