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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.pulls.review_comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.review_comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `_links` | `object` |  |
| `body_text` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `diff_hunk` | `string` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `pull_request_review_id` | `integer` |  |
| `original_commit_id` | `string` |  |
| `in_reply_to_id` | `integer` |  |
| `pull_request_url` | `string` |  |
| `node_id` | `string` |  |
| `body_html` | `string` |  |
| `url` | `string` |  |
| `body` | `string` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `position` | `integer` |  |
| `path` | `string` |  |
| `original_position` | `integer` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `commit_id` | `string` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `reactions` | `object` |  |
| `user` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_comments_for_review` | `owner, pull_number, repo, review_id` | List comments for a specific pull request review. | SELECT |
