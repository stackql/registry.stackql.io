---
title: legacy_projects
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
<tr><td><b>Name</b></td><td><code>github.teams.legacy_projects</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_projects</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `columns_url` | `string` |  |
| `html_url` | `string` |  |
| `body` | `string` |  |
| `url` | `string` |  |
| `permissions` | `object` |  |
| `state` | `string` |  |
| `private` | `boolean` | Whether the project is private or not. Only present when owner is an organization. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `organization_permission` | `string` | The organization permission for this project. Only present when owner is an organization. |
| `owner_url` | `string` |  |
| `creator` | `object` | Simple User |
| `number` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_projects_legacy` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://docs.github.com/rest/reference/teams#list-team-projects) endpoint.<br /><br />Lists the organization projects for a team. | SELECT |
| `remove_project_legacy` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/rest/reference/teams#remove-a-project-from-a-team) endpoint.<br /><br />Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it. | DELETE |
| `add_or_update_project_permissions_legacy` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/rest/reference/teams#add-or-update-team-project-permissions) endpoint.<br /><br />Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization. | EXEC |
| `check_permissions_for_project_legacy` | `project_id, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-project) endpoint.<br /><br />Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team. | EXEC |
