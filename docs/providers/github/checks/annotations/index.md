---
title: annotations
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
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.checks.annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `end_column` | `integer` |
| `raw_details` | `string` |
| `end_line` | `integer` |
| `path` | `string` |
| `title` | `string` |
| `start_column` | `integer` |
| `start_line` | `integer` |
| `blob_href` | `string` |
| `annotation_level` | `string` |
| `message` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_annotations` | `SELECT` | `check_run_id, owner, repo` |
