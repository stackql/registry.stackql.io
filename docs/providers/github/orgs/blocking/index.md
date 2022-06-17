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
<tr><td><b>Name</b></td><td><code>github.orgs.blocking</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.blocking</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `gists_url` | `string` |  |
| `gravatar_id` | `string` |  |
| `url` | `string` |  |
| `repos_url` | `string` |  |
| `organizations_url` | `string` |  |
| `avatar_url` | `string` |  |
| `starred_url` | `string` |  |
| `email` | `string` |  |
| `starred_at` | `string` |  |
| `subscriptions_url` | `string` |  |
| `followers_url` | `string` |  |
| `site_admin` | `boolean` |  |
| `html_url` | `string` |  |
| `events_url` | `string` |  |
| `received_events_url` | `string` |  |
| `login` | `string` |  |
| `node_id` | `string` |  |
| `following_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_blocked_users` | `org` | List the users blocked by an organization. | SELECT |
| `block_user` | `org, username` |  | EXEC |
| `check_blocked_user` | `org, username` |  | EXEC |
| `unblock_user` | `org, username` |  | EXEC |
