---
title: failed_invitations
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
<tr><td><b>Name</b></td><td><code>failed_invitations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.failed_invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `role` | `string` |  |
| `team_count` | `integer` |  |
| `email` | `string` |  |
| `login` | `string` |  |
| `node_id` | `string` |  |
| `failed_at` | `string` |  |
| `invitation_teams_url` | `string` |  |
| `inviter` | `object` | Simple User |
| `created_at` | `string` |  |
| `failed_reason` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_failed_invitations` | `SELECT` | `org` |
