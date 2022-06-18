---
title: tasklists
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
<tr><td><b>Name</b></td><td><code>tasklists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.tasks.tasklists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Task list identifier. |
| `title` | `string` | Title of the task list. |
| `updated` | `string` | Last modification time of the task list (as a RFC 3339 timestamp). |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | Type of the resource. This is always "tasks#taskList". |
| `selfLink` | `string` | URL pointing to this task list. Used to retrieve, update, or delete this task list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `tasklist` | Returns the authenticated user's specified task list. |
| `list` | `SELECT` |  | Returns all the authenticated user's task lists. |
| `insert` | `INSERT` |  | Creates a new task list and adds it to the authenticated user's task lists. |
| `delete` | `DELETE` | `tasklist` | Deletes the authenticated user's specified task list. |
| `patch` | `EXEC` | `tasklist` | Updates the authenticated user's specified task list. This method supports patch semantics. |
| `update` | `EXEC` | `tasklist` | Updates the authenticated user's specified task list. |
