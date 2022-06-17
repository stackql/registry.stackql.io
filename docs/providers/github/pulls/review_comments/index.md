---
title: review_comments
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
<tr><td><b>Name</b></td><td><code>review_comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.review_comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `body_html` | `string` |  |
| `url` | `string` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `author_association` | `string` | How the author is associated with the repository. |
| `pull_request_review_id` | `integer` |  |
| `original_commit_id` | `string` |  |
| `pull_request_url` | `string` |  |
| `body_text` | `string` |  |
| `node_id` | `string` |  |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `reactions` | `object` |  |
| `path` | `string` |  |
| `position` | `integer` |  |
| `_links` | `object` |  |
| `body` | `string` |  |
| `diff_hunk` | `string` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `user` | `object` | Simple User |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `in_reply_to_id` | `integer` |  |
| `original_position` | `integer` |  |
| `commit_id` | `string` |  |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `created_at` | `string` |  |
## Methods
