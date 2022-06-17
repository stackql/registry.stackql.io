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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.gists.comments</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.comments</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `user` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `body` | `string` | The comment text. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_comment` | `comment_id, gist_id` |  | SELECT |
| `list_comments` | `gist_id` |  | SELECT |
| `create_comment` | `gist_id, data__body` |  | INSERT |
| `delete_comment` | `comment_id, gist_id` |  | DELETE |
| `update_comment` | `comment_id, gist_id, data__body` |  | EXEC |
