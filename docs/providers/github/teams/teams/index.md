---
title: teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.teams</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `created_at` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `slug` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` | URL for the team |
| `repositories_url` | `string` |  |
| `organization` | `object` | Organization Full |
| `members_url` | `string` |  |
| `privacy` | `string` | The level of privacy this team should have |
| `permission` | `string` | Permission that the team will have for its repositories |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `node_id` | `string` |  |
| `repos_count` | `integer` |  |
| `updated_at` | `string` |  |
| `members_count` | `integer` |  |
## Methods
