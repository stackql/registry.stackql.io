---
title: invitation_teams
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
<tr><td><b>Name</b></td><td><code>github.orgs.invitation_teams</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.invitation_teams</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `slug` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `node_id` | `string` |  |
| `repositories_url` | `string` |  |
| `permissions` | `object` |  |
| `permission` | `string` |  |
| `html_url` | `string` |  |
| `members_url` | `string` |  |
| `url` | `string` |  |
| `privacy` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_invitation_teams` | `invitation_id, org` | List all teams associated with an invitation. In order to see invitations in an organization, the authenticated user must be an organization owner. | SELECT |
