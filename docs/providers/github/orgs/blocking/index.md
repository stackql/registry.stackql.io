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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.blocking</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `subscriptions_url` | `string` |
| `following_url` | `string` |
| `gists_url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
| `organizations_url` | `string` |
| `html_url` | `string` |
| `site_admin` | `boolean` |
| `received_events_url` | `string` |
| `repos_url` | `string` |
| `login` | `string` |
| `avatar_url` | `string` |
| `followers_url` | `string` |
| `url` | `string` |
| `events_url` | `string` |
| `starred_url` | `string` |
| `email` | `string` |
| `node_id` | `string` |
| `gravatar_id` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_blocked_users` | `SELECT` | `org` | List the users blocked by an organization. |
| `block_user` | `EXEC` | `org, username` |  |
| `check_blocked_user` | `EXEC` | `org, username` |  |
| `unblock_user` | `EXEC` | `org, username` |  |
