---
title: legacy_teams
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>legacy_teams</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_teams</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `members_count` | `integer` |  |
| `members_url` | `string` |  |
| `slug` | `string` |  |
| `url` | `string` | URL for the team |
| `repos_count` | `integer` |  |
| `html_url` | `string` |  |
| `repositories_url` | `string` |  |
| `organization` | `object` | Organization Full |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `permission` | `string` | Permission that the team will have for its repositories |
| `node_id` | `string` |  |
## Methods
