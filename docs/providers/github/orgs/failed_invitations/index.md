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
<tr><td><b>Name</b></td><td><code>github.orgs.failed_invitations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.failed_invitations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `invitation_teams_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `email` | `string` |  |
| `failed_reason` | `string` |  |
| `login` | `string` |  |
| `role` | `string` |  |
| `team_count` | `integer` |  |
| `inviter` | `object` | Simple User |
| `failed_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_failed_invitations` | `org` | The return hash contains `failed_at` and `failed_reason` fields which represent the time at which the invitation failed and the reason for the failure. | SELECT |
