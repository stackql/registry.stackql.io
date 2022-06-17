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
<tr><td><b>Name</b></td><td><code>github.orgs.public_members</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.public_members</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `starred_at` | `string` |  |
| `gravatar_id` | `string` |  |
| `url` | `string` |  |
| `followers_url` | `string` |  |
| `received_events_url` | `string` |  |
| `events_url` | `string` |  |
| `subscriptions_url` | `string` |  |
| `email` | `string` |  |
| `html_url` | `string` |  |
| `organizations_url` | `string` |  |
| `repos_url` | `string` |  |
| `type` | `string` |  |
| `gists_url` | `string` |  |
| `following_url` | `string` |  |
| `starred_url` | `string` |  |
| `node_id` | `string` |  |
| `site_admin` | `boolean` |  |
| `avatar_url` | `string` |  |
| `login` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_public_members` | `org` | Members of an organization can choose to have their membership publicized or not. | SELECT |
