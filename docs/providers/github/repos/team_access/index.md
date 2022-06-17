---
title: team_access
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
<tr><td><b>Name</b></td><td><code>github.repos.team_access</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.team_access</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `members_url` | `string` |  |
| `html_url` | `string` |  |
| `repositories_url` | `string` |  |
| `url` | `string` |  |
| `privacy` | `string` |  |
| `slug` | `string` |  |
| `parent` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `permission` | `string` |  |
| `node_id` | `string` |  |
| `permissions` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_teams_with_access_to_protected_branch` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists the teams who have push access to this branch. The list includes child teams. | SELECT |
| `add_team_access_restrictions` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Grants the specified teams push access for this branch. You can also give push access to child teams.<br /><br />\| Type    \| Description                                                                                                                                \|<br />\| ------- \| ------------------------------------------------------------------------------------------------------------------------------------------ \|<br />\| `array` \| The teams that can have push access. Use the team's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| | INSERT |
| `remove_team_access_restrictions` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Removes the ability of a team to push to this branch. You can also remove push access for child teams.<br /><br />\| Type    \| Description                                                                                                                                         \|<br />\| ------- \| --------------------------------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Teams that should no longer have push access. Use the team's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| | DELETE |
| `set_team_access_restrictions` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Replaces the list of teams that have push access to this branch. This removes all teams that previously had push access and grants push access to the new list of teams. Team restrictions include child teams.<br /><br />\| Type    \| Description                                                                                                                                \|<br />\| ------- \| ------------------------------------------------------------------------------------------------------------------------------------------ \|<br />\| `array` \| The teams that can have push access. Use the team's `slug`. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| | EXEC |
