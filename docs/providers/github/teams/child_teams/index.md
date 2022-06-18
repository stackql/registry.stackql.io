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
<tr><td><b>Name</b></td><td><code>child_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.child_teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `slug` | `string` |  |
| `permission` | `string` |  |
| `permissions` | `object` |  |
| `members_url` | `string` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `privacy` | `string` |  |
| `repositories_url` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_child_in_org` | `SELECT` | `org, team_slug` |
