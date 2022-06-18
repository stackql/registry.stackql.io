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
<tr><td><b>Name</b></td><td><code>review_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.review_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `_links` | `object` |  |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `url` | `string` |  |
| `original_commit_id` | `string` |  |
| `commit_id` | `string` |  |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `created_at` | `string` |  |
| `in_reply_to_id` | `integer` |  |
| `reactions` | `object` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `original_position` | `integer` |  |
| `user` | `object` | Simple User |
| `body_html` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `node_id` | `string` |  |
| `position` | `integer` |  |
| `diff_hunk` | `string` |  |
| `body` | `string` |  |
| `pull_request_review_id` | `integer` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `html_url` | `string` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `body_text` | `string` |  |
| `updated_at` | `string` |  |
| `path` | `string` |  |
| `pull_request_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_comments_for_review` | `SELECT` | `owner, pull_number, repo, review_id` |
