---
title: members
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `url` | `string` |
| `starred_url` | `string` |
| `avatar_url` | `string` |
| `following_url` | `string` |
| `received_events_url` | `string` |
| `gravatar_id` | `string` |
| `events_url` | `string` |
| `starred_at` | `string` |
| `html_url` | `string` |
| `login` | `string` |
| `repos_url` | `string` |
| `gists_url` | `string` |
| `followers_url` | `string` |
| `node_id` | `string` |
| `site_admin` | `boolean` |
| `subscriptions_url` | `string` |
| `type` | `string` |
| `organizations_url` | `string` |
| `email` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_members` | `SELECT` | `org` | List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned. |
| `remove_member` | `DELETE` | `org, username` | Removing a user from this list will remove them from all teams and they will no longer have any access to the organization's repositories. |
