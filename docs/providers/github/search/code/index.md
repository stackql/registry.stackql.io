---
title: code
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
<tr><td><b>Name</b></td><td><code>code</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.code</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `last_modified_at` | `string` |  |
| `path` | `string` |  |
| `sha` | `string` |  |
| `text_matches` | `array` |  |
| `repository` | `object` | Minimal Repository |
| `file_size` | `integer` |  |
| `score` | `number` |  |
| `git_url` | `string` |  |
| `html_url` | `string` |  |
| `line_numbers` | `array` |  |
| `url` | `string` |  |
| `language` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `code` | `SELECT` | `q` |
