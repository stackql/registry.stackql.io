---
title: user_access
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
<tr><td><b>Name</b></td><td><code>github.repos.user_access</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.user_access</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `site_admin` | `boolean` |  |
| `organizations_url` | `string` |  |
| `starred_url` | `string` |  |
| `node_id` | `string` |  |
| `received_events_url` | `string` |  |
| `avatar_url` | `string` |  |
| `email` | `string` |  |
| `followers_url` | `string` |  |
| `url` | `string` |  |
| `following_url` | `string` |  |
| `starred_at` | `string` |  |
| `gravatar_id` | `string` |  |
| `gists_url` | `string` |  |
| `events_url` | `string` |  |
| `html_url` | `string` |  |
| `repos_url` | `string` |  |
| `login` | `string` |  |
| `type` | `string` |  |
| `subscriptions_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_users_with_access_to_protected_branch` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists the people who have push access to this branch. | SELECT |
| `add_user_access_restrictions` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Grants the specified people push access for this branch.<br /><br />\| Type    \| Description                                                                                                                   \|<br />\| ------- \| ----------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| | INSERT |
| `remove_user_access_restrictions` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Removes the ability of a user to push to this branch.<br /><br />\| Type    \| Description                                                                                                                                   \|<br />\| ------- \| --------------------------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| | DELETE |
| `set_user_access_restrictions` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Replaces the list of people that have push access to this branch. This removes all people that previously had push access and grants push access to the new list of people.<br /><br />\| Type    \| Description                                                                                                                   \|<br />\| ------- \| ----------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| | EXEC |
