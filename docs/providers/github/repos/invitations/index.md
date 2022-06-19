---
title: invitations
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository invitation. |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `invitee` | `object` | Simple User |
| `repository` | `object` | Minimal Repository |
| `permissions` | `string` | The permission associated with the invitation. |
| `expired` | `boolean` | Whether or not the invitation has expired |
| `inviter` | `object` | Simple User |
| `url` | `string` | URL for the repository invitation |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_invitations` | `SELECT` | `owner, repo` | When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations. |
| `list_invitations_for_authenticated_user` | `SELECT` |  | When authenticating as a user, this endpoint will list all currently open repository invitations for that user. |
| `delete_invitation` | `DELETE` | `invitation_id, owner, repo` |  |
| `accept_invitation_for_authenticated_user` | `EXEC` | `invitation_id` |  |
| `decline_invitation_for_authenticated_user` | `EXEC` | `invitation_id` |  |
| `update_invitation` | `EXEC` | `invitation_id, owner, repo` |  |
