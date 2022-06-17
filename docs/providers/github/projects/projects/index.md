---
title: projects
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
<tr><td><b>Name</b></td><td><code>github.projects.projects</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.projects</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` | Name of the project |
| `node_id` | `string` |  |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `creator` | `object` | Simple User |
| `owner_url` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `number` | `integer` |  |
| `body` | `string` | Body of the project |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `columns_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `project_id` | Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. | SELECT |
| `list_for_org` | `org` | Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. | SELECT |
| `list_for_repo` | `owner, repo` | Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. | SELECT |
| `list_for_user` | `username` |  | SELECT |
| `create_for_authenticated_user` | `data__name` |  | INSERT |
| `create_for_org` | `org, data__name` | Creates an organization project board. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. | INSERT |
| `create_for_repo` | `owner, repo, data__name` | Creates a repository project board. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. | INSERT |
| `delete` | `project_id` | Deletes a project board. Returns a `404 Not Found` status if projects are disabled. | DELETE |
| `update` | `project_id` | Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. | EXEC |
