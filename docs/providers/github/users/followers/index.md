---
title: followers
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
<tr><td><b>Name</b></td><td><code>followers</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.users.followers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `email` | `string` |
| `received_events_url` | `string` |
| `node_id` | `string` |
| `following_url` | `string` |
| `subscriptions_url` | `string` |
| `type` | `string` |
| `starred_at` | `string` |
| `events_url` | `string` |
| `repos_url` | `string` |
| `starred_url` | `string` |
| `login` | `string` |
| `gists_url` | `string` |
| `url` | `string` |
| `organizations_url` | `string` |
| `site_admin` | `boolean` |
| `avatar_url` | `string` |
| `gravatar_id` | `string` |
| `html_url` | `string` |
| `followers_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_followers_for_authenticated_user` | `SELECT` |  | Lists the people following the authenticated user. |
| `list_followers_for_user` | `SELECT` | `username` | Lists the people following the specified user. |
