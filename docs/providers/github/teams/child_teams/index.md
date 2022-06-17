---
title: child_teams
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
<tr><td><b>Name</b></td><td><code>github.teams.child_teams</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.child_teams</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `slug` | `string` |  |
| `url` | `string` |  |
| `permission` | `string` |  |
| `privacy` | `string` |  |
| `node_id` | `string` |  |
| `permissions` | `object` |  |
| `repositories_url` | `string` |  |
| `html_url` | `string` |  |
| `members_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_child_in_org` | `org, team_slug` | Lists the child teams of the team specified by `{team_slug}`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/teams`. | SELECT |
