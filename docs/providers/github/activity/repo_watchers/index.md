---
title: repo_watchers
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
<tr><td><b>Name</b></td><td><code>repo_watchers</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repo_watchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `starred_url` | `string` |
| `following_url` | `string` |
| `repos_url` | `string` |
| `received_events_url` | `string` |
| `gists_url` | `string` |
| `site_admin` | `boolean` |
| `node_id` | `string` |
| `url` | `string` |
| `email` | `string` |
| `followers_url` | `string` |
| `type` | `string` |
| `organizations_url` | `string` |
| `starred_at` | `string` |
| `html_url` | `string` |
| `login` | `string` |
| `subscriptions_url` | `string` |
| `events_url` | `string` |
| `gravatar_id` | `string` |
| `avatar_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_watchers_for_repo` | `SELECT` | `owner, repo` |
