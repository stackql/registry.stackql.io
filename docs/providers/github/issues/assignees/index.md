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
<tr><td><b>Name</b></td><td><code>assignees</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.assignees</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `avatar_url` | `string` |
| `gists_url` | `string` |
| `gravatar_id` | `string` |
| `following_url` | `string` |
| `site_admin` | `boolean` |
| `events_url` | `string` |
| `login` | `string` |
| `email` | `string` |
| `node_id` | `string` |
| `organizations_url` | `string` |
| `url` | `string` |
| `followers_url` | `string` |
| `received_events_url` | `string` |
| `repos_url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
| `html_url` | `string` |
| `subscriptions_url` | `string` |
| `starred_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_assignees` | `SELECT` | `owner, repo` | Lists the [available assignees](https://docs.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository. |
| `add_assignees` | `INSERT` | `issue_number, owner, repo` | Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced. |
| `remove_assignees` | `DELETE` | `issue_number, owner, repo` | Removes one or more assignees from an issue. |
| `check_user_can_be_assigned` | `EXEC` | `assignee, owner, repo` | Checks if a user has permission to be assigned to an issue in this repository.<br /><br />If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.<br /><br />Otherwise a `404` status code is returned. |
