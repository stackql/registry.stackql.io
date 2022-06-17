---
title: columns
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
<tr><td><b>Name</b></td><td><code>github.projects.columns</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.columns</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The unique identifier of the project column |
| `name` | `string` | Name of the project column |
| `node_id` | `string` |  |
| `project_url` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `cards_url` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_column` | `column_id` |  | SELECT |
| `list_columns` | `project_id` |  | SELECT |
| `create_column` | `project_id, data__name` |  | INSERT |
| `delete_column` | `column_id` |  | DELETE |
| `move_column` | `column_id, data__position` |  | EXEC |
| `update_column` | `column_id, data__name` |  | EXEC |
