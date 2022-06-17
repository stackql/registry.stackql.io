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
<tr><td><b>Name</b></td><td><code>blocking</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.blocking</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `subscriptions_url` | `string` |
| `login` | `string` |
| `starred_url` | `string` |
| `gists_url` | `string` |
| `received_events_url` | `string` |
| `url` | `string` |
| `gravatar_id` | `string` |
| `node_id` | `string` |
| `organizations_url` | `string` |
| `starred_at` | `string` |
| `avatar_url` | `string` |
| `email` | `string` |
| `repos_url` | `string` |
| `html_url` | `string` |
| `type` | `string` |
| `followers_url` | `string` |
| `site_admin` | `boolean` |
| `events_url` | `string` |
| `following_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_blocked_users` | `SELECT` | `org` | List the users blocked by an organization. |
| `block_user` | `EXEC` | `org, username` |  |
| `check_blocked_user` | `EXEC` | `org, username` |  |
| `unblock_user` | `EXEC` | `org, username` |  |
