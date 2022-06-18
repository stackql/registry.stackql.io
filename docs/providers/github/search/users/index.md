---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `hireable` | `boolean` |
| `updated_at` | `string` |
| `following` | `integer` |
| `blog` | `string` |
| `email` | `string` |
| `text_matches` | `array` |
| `starred_url` | `string` |
| `organizations_url` | `string` |
| `score` | `number` |
| `node_id` | `string` |
| `type` | `string` |
| `created_at` | `string` |
| `avatar_url` | `string` |
| `public_repos` | `integer` |
| `gravatar_id` | `string` |
| `public_gists` | `integer` |
| `events_url` | `string` |
| `html_url` | `string` |
| `repos_url` | `string` |
| `received_events_url` | `string` |
| `company` | `string` |
| `followers` | `integer` |
| `login` | `string` |
| `suspended_at` | `string` |
| `subscriptions_url` | `string` |
| `following_url` | `string` |
| `site_admin` | `boolean` |
| `gists_url` | `string` |
| `followers_url` | `string` |
| `url` | `string` |
| `location` | `string` |
| `bio` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `users` | `SELECT` | `q` |
