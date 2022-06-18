---
title: blobs
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
<tr><td><b>Name</b></td><td><code>blobs</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.git.blobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `url` | `string` |
| `content` | `string` |
| `encoding` | `string` |
| `highlighted_content` | `string` |
| `node_id` | `string` |
| `sha` | `string` |
| `size` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get_blob` | `SELECT` | `file_sha, owner, repo` | The `content` in the response will always be Base64 encoded.<br /><br />_Note_: This API supports blobs up to 100 megabytes in size. |
| `create_blob` | `INSERT` | `owner, repo, data__content` |  |
