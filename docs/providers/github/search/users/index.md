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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `repos_url` | `string` |
| `hireable` | `boolean` |
| `gravatar_id` | `string` |
| `type` | `string` |
| `score` | `number` |
| `suspended_at` | `string` |
| `text_matches` | `array` |
| `site_admin` | `boolean` |
| `following_url` | `string` |
| `avatar_url` | `string` |
| `public_repos` | `integer` |
| `email` | `string` |
| `public_gists` | `integer` |
| `subscriptions_url` | `string` |
| `following` | `integer` |
| `login` | `string` |
| `html_url` | `string` |
| `followers` | `integer` |
| `starred_url` | `string` |
| `blog` | `string` |
| `bio` | `string` |
| `url` | `string` |
| `events_url` | `string` |
| `updated_at` | `string` |
| `company` | `string` |
| `created_at` | `string` |
| `organizations_url` | `string` |
| `gists_url` | `string` |
| `followers_url` | `string` |
| `location` | `string` |
| `node_id` | `string` |
| `received_events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `users` | `SELECT` | `q` |
