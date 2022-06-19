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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repo_watchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `gravatar_id` | `string` |
| `type` | `string` |
| `following_url` | `string` |
| `html_url` | `string` |
| `email` | `string` |
| `repos_url` | `string` |
| `avatar_url` | `string` |
| `subscriptions_url` | `string` |
| `starred_at` | `string` |
| `login` | `string` |
| `node_id` | `string` |
| `received_events_url` | `string` |
| `url` | `string` |
| `site_admin` | `boolean` |
| `gists_url` | `string` |
| `events_url` | `string` |
| `organizations_url` | `string` |
| `followers_url` | `string` |
| `starred_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_watchers_for_repo` | `SELECT` | `owner, repo` |
