---
title: cards
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
<tr><td><b>Name</b></td><td><code>cards</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.cards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The project card's ID |
| `project_url` | `string` |  |
| `url` | `string` |  |
| `column_url` | `string` |  |
| `creator` | `object` | Simple User |
| `project_id` | `string` |  |
| `archived` | `boolean` | Whether or not the card is archived |
| `column_name` | `string` |  |
| `note` | `string` |  |
| `updated_at` | `string` |  |
| `content_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_card` | `SELECT` | `card_id` |
| `list_cards` | `SELECT` | `column_id` |
| `create_card` | `INSERT` | `column_id` |
| `delete_card` | `DELETE` | `card_id` |
| `move_card` | `EXEC` | `card_id, data__position` |
| `update_card` | `EXEC` | `card_id` |
