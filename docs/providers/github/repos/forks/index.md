---
title: forks
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
<tr><td><b>Name</b></td><td><code>forks</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.forks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `assignees_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `languages_url` | `string` |  |
| `ssh_url` | `string` |  |
| `downloads_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `created_at` | `string` |  |
| `forks` | `integer` |  |
| `deployments_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `compare_url` | `string` |  |
| `permissions` | `object` |  |
| `size` | `integer` |  |
| `private` | `boolean` |  |
| `role_name` | `string` |  |
| `has_wiki` | `boolean` |  |
| `blobs_url` | `string` |  |
| `visibility` | `string` |  |
| `git_refs_url` | `string` |  |
| `topics` | `array` |  |
| `clone_url` | `string` |  |
| `disabled` | `boolean` |  |
| `pushed_at` | `string` |  |
| `default_branch` | `string` |  |
| `forks_count` | `integer` |  |
| `issues_url` | `string` |  |
| `network_count` | `integer` |  |
| `fork` | `boolean` |  |
| `labels_url` | `string` |  |
| `contents_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `collaborators_url` | `string` |  |
| `node_id` | `string` |  |
| `trees_url` | `string` |  |
| `subscription_url` | `string` |  |
| `merges_url` | `string` |  |
| `owner` | `object` | Simple User |
| `license` | `object` |  |
| `watchers_count` | `integer` |  |
| `svn_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `keys_url` | `string` |  |
| `contributors_url` | `string` |  |
| `branches_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `tags_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `comments_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `events_url` | `string` |  |
| `open_issues` | `integer` |  |
| `archive_url` | `string` |  |
| `notifications_url` | `string` |  |
| `is_template` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `watchers` | `integer` |  |
| `releases_url` | `string` |  |
| `pulls_url` | `string` |  |
| `milestones_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `commits_url` | `string` |  |
| `archived` | `boolean` |  |
| `forks_url` | `string` |  |
| `homepage` | `string` |  |
| `statuses_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `full_name` | `string` |  |
| `teams_url` | `string` |  |
| `git_url` | `string` |  |
| `hooks_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `issue_comment_url` | `string` |  |
| `html_url` | `string` |  |
| `language` | `string` |  |
| `url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
