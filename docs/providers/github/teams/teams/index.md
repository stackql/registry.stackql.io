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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.teams.teams</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.teams</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` |  |
| `organization` | `object` | Organization Full |
| `members_count` | `integer` |  |
| `updated_at` | `string` |  |
| `repositories_url` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| `privacy` | `string` | The level of privacy this team should have |
| `url` | `string` | URL for the team |
| `node_id` | `string` |  |
| `permission` | `string` | Permission that the team will have for its repositories |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `repos_count` | `integer` |  |
| `members_url` | `string` |  |
| `slug` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_by_name` | `org, team_slug` | Gets a team using the team's `slug`. GitHub generates the `slug` from the team `name`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}`. | SELECT |
| `list` | `org` | Lists all teams in an organization that are visible to the authenticated user. | SELECT |
| `list_for_authenticated_user` | `` | List all of the teams across all of the organizations to which the authenticated user belongs. This method requires `user`, `repo`, or `read:org` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/apps/building-oauth-apps/). | SELECT |
| `create` | `org, data__name` | To create a team, the authenticated user must be a member or owner of `{org}`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see "[Setting team creation permissions](https://docs.github.com/en/articles/setting-team-creation-permissions-in-your-organization)."<br /><br />When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see "[About teams](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)". | INSERT |
| `delete_in_org` | `org, team_slug` | To delete a team, the authenticated user must be an organization owner or team maintainer.<br /><br />If you are an organization owner, deleting a parent team will delete all of its child teams as well.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}`. | DELETE |
| `update_in_org` | `org, team_slug` | To edit a team, the authenticated user must either be an organization owner or a team maintainer.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}`. | EXEC |
