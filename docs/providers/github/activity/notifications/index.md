---
title: notifications
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
<tr><td><b>Name</b></td><td><code>github.activity.notifications</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.notifications</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `updated_at` | `string` |  |
| `unread` | `boolean` |  |
| `url` | `string` |  |
| `subscription_url` | `string` |  |
| `reason` | `string` |  |
| `last_read_at` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `subject` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_thread` | `thread_id` |  | SELECT |
| `list_notifications_for_authenticated_user` | `` | List all notifications for the current user, sorted by most recently updated. | SELECT |
| `list_repo_notifications_for_authenticated_user` | `owner, repo` | List all notifications for the current user. | SELECT |
| `mark_notifications_as_read` | `` | Marks all notifications as "read" removes it from the [default view on GitHub](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/rest/reference/activity#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. | EXEC |
| `mark_repo_notifications_as_read` | `owner, repo` | Marks all notifications in a repository as "read" removes them from the [default view on GitHub](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/rest/reference/activity#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. | EXEC |
| `mark_thread_as_read` | `thread_id` |  | EXEC |
