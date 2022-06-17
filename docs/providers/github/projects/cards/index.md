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
<tr><td><b>Name</b></td><td><code>github.projects.cards</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.cards</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The project card's ID |
| `column_name` | `string` |  |
| `note` | `string` |  |
| `archived` | `boolean` | Whether or not the card is archived |
| `project_id` | `string` |  |
| `content_url` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `project_url` | `string` |  |
| `url` | `string` |  |
| `creator` | `object` | Simple User |
| `column_url` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_card` | `card_id` |  | SELECT |
| `list_cards` | `column_id` |  | SELECT |
| `create_card` | `column_id` |  | INSERT |
| `delete_card` | `card_id` |  | DELETE |
| `move_card` | `card_id, data__position` |  | EXEC |
| `update_card` | `card_id` |  | EXEC |
