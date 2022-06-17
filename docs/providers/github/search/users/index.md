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
| `email` | `string` |
| `site_admin` | `boolean` |
| `organizations_url` | `string` |
| `avatar_url` | `string` |
| `followers` | `integer` |
| `subscriptions_url` | `string` |
| `blog` | `string` |
| `node_id` | `string` |
| `following` | `integer` |
| `events_url` | `string` |
| `login` | `string` |
| `starred_url` | `string` |
| `public_gists` | `integer` |
| `url` | `string` |
| `followers_url` | `string` |
| `bio` | `string` |
| `following_url` | `string` |
| `gravatar_id` | `string` |
| `location` | `string` |
| `public_repos` | `integer` |
| `text_matches` | `array` |
| `html_url` | `string` |
| `type` | `string` |
| `received_events_url` | `string` |
| `updated_at` | `string` |
| `suspended_at` | `string` |
| `score` | `number` |
| `company` | `string` |
| `created_at` | `string` |
| `repos_url` | `string` |
| `gists_url` | `string` |
| `hireable` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `users` | `SELECT` | `q` |
