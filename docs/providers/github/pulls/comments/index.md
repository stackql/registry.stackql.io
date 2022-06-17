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
<tr><td><b>Id</b></td><td><code>github.pulls.comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the pull request review comment. |
| `original_line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `reactions` | `object` |  |
| `_links` | `object` |  |
| `body_html` | `string` |  |
| `commit_id` | `string` | The SHA of the commit to which the comment applies. |
| `body` | `string` | The text of the comment. |
| `in_reply_to_id` | `integer` | The comment ID to reply to. |
| `url` | `string` | URL for the pull request review comment |
| `body_text` | `string` |  |
| `node_id` | `string` | The node ID of the pull request review comment. |
| `diff_hunk` | `string` | The diff of the line that the comment refers to. |
| `pull_request_review_id` | `integer` | The ID of the pull request review to which the comment belongs. |
| `original_start_line` | `integer` | The first line of the range for a multi-line comment. |
| `created_at` | `string` |  |
| `path` | `string` | The relative path of the file to which the comment applies. |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `pull_request_url` | `string` | URL for the pull request that the review comment belongs to. |
| `original_position` | `integer` | The index of the original line in the diff to which the comment applies. |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `side` | `string` | The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment |
| `author_association` | `string` | How the author is associated with the repository. |
| `original_commit_id` | `string` | The SHA of the original commit to which the comment applies. |
| `user` | `object` | Simple User |
| `updated_at` | `string` |  |
| `html_url` | `string` | HTML URL for the pull request review comment. |
| `position` | `integer` | The line index in the diff to which the comment applies. |
## Methods
