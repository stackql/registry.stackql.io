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
<tr><td><b>Name</b></td><td><code>milestones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.milestones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `description` | `string` |  |
| `labels_url` | `string` |  |
| `html_url` | `string` |  |
| `open_issues` | `integer` |  |
| `state` | `string` | The state of the milestone. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `due_on` | `string` |  |
| `closed_issues` | `integer` |  |
| `closed_at` | `string` |  |
| `number` | `integer` | The number of the milestone. |
| `title` | `string` | The title of the milestone. |
| `url` | `string` |  |
| `creator` | `object` | Simple User |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_milestone` | `SELECT` | `milestone_number, owner, repo` |
| `list_milestones` | `SELECT` | `owner, repo` |
| `create_milestone` | `INSERT` | `owner, repo, data__title` |
| `delete_milestone` | `DELETE` | `milestone_number, owner, repo` |
| `update_milestone` | `EXEC` | `milestone_number, owner, repo` |
