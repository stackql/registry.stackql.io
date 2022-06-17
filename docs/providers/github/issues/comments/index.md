---
title: comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the issue comment |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `user` | `object` | Simple User |
| `updated_at` | `string` |  |
| `url` | `string` | URL for the issue comment |
| `html_url` | `string` |  |
| `reactions` | `object` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `issue_url` | `string` |  |
| `body_text` | `string` |  |
| `body` | `string` | Contents of the issue comment |
| `body_html` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
## Methods
