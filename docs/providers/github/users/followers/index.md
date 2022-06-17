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
<tr><td><b>Name</b></td><td><code>github.users.followers</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.users.followers</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `gists_url` | `string` |  |
| `avatar_url` | `string` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
| `subscriptions_url` | `string` |  |
| `starred_at` | `string` |  |
| `site_admin` | `boolean` |  |
| `email` | `string` |  |
| `followers_url` | `string` |  |
| `type` | `string` |  |
| `following_url` | `string` |  |
| `organizations_url` | `string` |  |
| `repos_url` | `string` |  |
| `starred_url` | `string` |  |
| `events_url` | `string` |  |
| `gravatar_id` | `string` |  |
| `login` | `string` |  |
| `node_id` | `string` |  |
| `received_events_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_followers_for_authenticated_user` | `` | Lists the people following the authenticated user. | SELECT |
| `list_followers_for_user` | `username` | Lists the people following the specified user. | SELECT |
