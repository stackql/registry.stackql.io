---
title: public_members
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
<tr><td><b>Name</b></td><td><code>public_members</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.public_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `repos_url` | `string` |
| `organizations_url` | `string` |
| `avatar_url` | `string` |
| `site_admin` | `boolean` |
| `email` | `string` |
| `followers_url` | `string` |
| `login` | `string` |
| `following_url` | `string` |
| `html_url` | `string` |
| `type` | `string` |
| `node_id` | `string` |
| `url` | `string` |
| `gists_url` | `string` |
| `starred_at` | `string` |
| `starred_url` | `string` |
| `subscriptions_url` | `string` |
| `received_events_url` | `string` |
| `gravatar_id` | `string` |
| `events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public_members` | `SELECT` | `org` |
