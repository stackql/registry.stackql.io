---
title: contributors
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
<tr><td><b>Name</b></td><td><code>contributors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.contributors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `received_events_url` | `string` |
| `type` | `string` |
| `node_id` | `string` |
| `organizations_url` | `string` |
| `html_url` | `string` |
| `subscriptions_url` | `string` |
| `url` | `string` |
| `site_admin` | `boolean` |
| `events_url` | `string` |
| `gravatar_id` | `string` |
| `contributions` | `integer` |
| `following_url` | `string` |
| `followers_url` | `string` |
| `repos_url` | `string` |
| `login` | `string` |
| `gists_url` | `string` |
| `avatar_url` | `string` |
| `email` | `string` |
| `starred_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_contributors` | `SELECT` | `owner, repo` |
