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
<tr><td><b>Name</b></td><td><code>github.git.blobs</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.git.blobs</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `highlighted_content` | `string` |  |
| `node_id` | `string` |  |
| `sha` | `string` |  |
| `size` | `integer` |  |
| `url` | `string` |  |
| `content` | `string` |  |
| `encoding` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_blob` | `file_sha, owner, repo` | The `content` in the response will always be Base64 encoded.<br /><br />_Note_: This API supports blobs up to 100 megabytes in size. | SELECT |
| `create_blob` | `owner, repo, data__content` |  | INSERT |
