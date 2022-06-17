---
title: blocking
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
<tr><td><b>Name</b></td><td><code>github.users.blocking</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.users.blocking</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `email` | `string` |  |
| `subscriptions_url` | `string` |  |
| `following_url` | `string` |  |
| `gists_url` | `string` |  |
| `site_admin` | `boolean` |  |
| `url` | `string` |  |
| `type` | `string` |  |
| `starred_at` | `string` |  |
| `gravatar_id` | `string` |  |
| `organizations_url` | `string` |  |
| `repos_url` | `string` |  |
| `node_id` | `string` |  |
| `followers_url` | `string` |  |
| `login` | `string` |  |
| `received_events_url` | `string` |  |
| `starred_url` | `string` |  |
| `events_url` | `string` |  |
| `html_url` | `string` |  |
| `avatar_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_blocked_by_authenticated_user` | `` | List the users you've blocked on your personal account. | SELECT |
| `block` | `username` |  | EXEC |
| `check_blocked` | `username` |  | EXEC |
| `unblock` | `username` |  | EXEC |
