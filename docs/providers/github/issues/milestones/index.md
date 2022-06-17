---
title: milestones
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
<tr><td><b>Name</b></td><td><code>github.issues.milestones</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.milestones</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `description` | `string` |  |
| `closed_issues` | `integer` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `open_issues` | `integer` |  |
| `html_url` | `string` |  |
| `number` | `integer` | The number of the milestone. |
| `created_at` | `string` |  |
| `closed_at` | `string` |  |
| `state` | `string` | The state of the milestone. |
| `title` | `string` | The title of the milestone. |
| `creator` | `object` | Simple User |
| `due_on` | `string` |  |
| `node_id` | `string` |  |
| `labels_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_milestone` | `milestone_number, owner, repo` |  | SELECT |
| `list_milestones` | `owner, repo` |  | SELECT |
| `create_milestone` | `owner, repo, data__title` |  | INSERT |
| `delete_milestone` | `milestone_number, owner, repo` |  | DELETE |
| `update_milestone` | `milestone_number, owner, repo` |  | EXEC |
