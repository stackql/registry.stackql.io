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
| `gravatar_id` | `string` |
| `public_gists` | `integer` |
| `created_at` | `string` |
| `site_admin` | `boolean` |
| `repos_url` | `string` |
| `company` | `string` |
| `gists_url` | `string` |
| `organizations_url` | `string` |
| `received_events_url` | `string` |
| `html_url` | `string` |
| `suspended_at` | `string` |
| `updated_at` | `string` |
| `followers_url` | `string` |
| `following` | `integer` |
| `starred_url` | `string` |
| `blog` | `string` |
| `subscriptions_url` | `string` |
| `score` | `number` |
| `text_matches` | `array` |
| `events_url` | `string` |
| `avatar_url` | `string` |
| `email` | `string` |
| `node_id` | `string` |
| `bio` | `string` |
| `public_repos` | `integer` |
| `following_url` | `string` |
| `url` | `string` |
| `type` | `string` |
| `location` | `string` |
| `hireable` | `boolean` |
| `login` | `string` |
| `followers` | `integer` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `users` | `SELECT` | `q` |
