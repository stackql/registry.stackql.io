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
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `commit_id` | `string` |  |
| `url` | `string` |  |
| `body_html` | `string` |  |
| `position` | `integer` |  |
| `html_url` | `string` |  |
| `path` | `string` |  |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `author_association` | `string` | How the author is associated with the repository. |
| `reactions` | `object` |  |
| `updated_at` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `original_commit_id` | `string` |  |
| `body_text` | `string` |  |
| `in_reply_to_id` | `integer` |  |
| `pull_request_review_id` | `integer` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `node_id` | `string` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `diff_hunk` | `string` |  |
| `created_at` | `string` |  |
| `original_position` | `integer` |  |
| `pull_request_url` | `string` |  |
| `_links` | `object` |  |
| `user` | `object` | Simple User |
| `body` | `string` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_comments_for_review` | `SELECT` | `owner, pull_number, repo, review_id` |
