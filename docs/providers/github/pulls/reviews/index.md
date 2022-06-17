---
title: reviews
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
<tr><td><b>Name</b></td><td><code>reviews</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.reviews</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the review |
| `pull_request_url` | `string` |  |
| `node_id` | `string` |  |
| `state` | `string` |  |
| `user` | `object` | Simple User |
| `body` | `string` | The text of the review. |
| `body_html` | `string` |  |
| `commit_id` | `string` | A commit SHA for the review. |
| `submitted_at` | `string` |  |
| `body_text` | `string` |  |
| `html_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `_links` | `object` |  |
## Methods
