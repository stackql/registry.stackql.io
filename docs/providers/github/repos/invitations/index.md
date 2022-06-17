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
<tr><td><b>Name</b></td><td><code>github.repos.invitations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.invitations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository invitation. |
| `expired` | `boolean` | Whether or not the invitation has expired |
| `inviter` | `object` | Simple User |
| `url` | `string` | URL for the repository invitation |
| `node_id` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `invitee` | `object` | Simple User |
| `permissions` | `string` | The permission associated with the invitation. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_invitations` | `owner, repo` | When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations. | SELECT |
| `list_invitations_for_authenticated_user` | `` | When authenticating as a user, this endpoint will list all currently open repository invitations for that user. | SELECT |
| `delete_invitation` | `invitation_id, owner, repo` |  | DELETE |
| `accept_invitation_for_authenticated_user` | `invitation_id` |  | EXEC |
| `decline_invitation_for_authenticated_user` | `invitation_id` |  | EXEC |
| `update_invitation` | `invitation_id, owner, repo` |  | EXEC |
