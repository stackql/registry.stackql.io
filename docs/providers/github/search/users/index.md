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
| `public_repos` | `integer` |
| `email` | `string` |
| `login` | `string` |
| `gravatar_id` | `string` |
| `events_url` | `string` |
| `score` | `number` |
| `following` | `integer` |
| `text_matches` | `array` |
| `subscriptions_url` | `string` |
| `hireable` | `boolean` |
| `location` | `string` |
| `gists_url` | `string` |
| `followers` | `integer` |
| `organizations_url` | `string` |
| `html_url` | `string` |
| `blog` | `string` |
| `url` | `string` |
| `public_gists` | `integer` |
| `created_at` | `string` |
| `following_url` | `string` |
| `updated_at` | `string` |
| `bio` | `string` |
| `repos_url` | `string` |
| `suspended_at` | `string` |
| `node_id` | `string` |
| `site_admin` | `boolean` |
| `starred_url` | `string` |
| `received_events_url` | `string` |
| `company` | `string` |
| `avatar_url` | `string` |
| `followers_url` | `string` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `users` | `SELECT` | `q` |
