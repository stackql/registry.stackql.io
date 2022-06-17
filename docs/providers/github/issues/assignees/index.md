---
title: assignees
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
<tr><td><b>Name</b></td><td><code>github.issues.assignees</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.assignees</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `starred_at` | `string` |  |
| `starred_url` | `string` |  |
| `gravatar_id` | `string` |  |
| `avatar_url` | `string` |  |
| `url` | `string` |  |
| `repos_url` | `string` |  |
| `gists_url` | `string` |  |
| `html_url` | `string` |  |
| `email` | `string` |  |
| `type` | `string` |  |
| `received_events_url` | `string` |  |
| `organizations_url` | `string` |  |
| `subscriptions_url` | `string` |  |
| `followers_url` | `string` |  |
| `node_id` | `string` |  |
| `site_admin` | `boolean` |  |
| `events_url` | `string` |  |
| `login` | `string` |  |
| `following_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_assignees` | `owner, repo` | Lists the [available assignees](https://docs.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository. | SELECT |
| `add_assignees` | `issue_number, owner, repo` | Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced. | INSERT |
| `remove_assignees` | `issue_number, owner, repo` | Removes one or more assignees from an issue. | DELETE |
| `check_user_can_be_assigned` | `assignee, owner, repo` | Checks if a user has permission to be assigned to an issue in this repository.<br /><br />If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.<br /><br />Otherwise a `404` status code is returned. | EXEC |
