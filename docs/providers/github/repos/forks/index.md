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
| `has_pages` | `boolean` |  |
| `archived` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `subscription_url` | `string` |  |
| `owner` | `object` | Simple User |
| `size` | `integer` |  |
| `hooks_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `pulls_url` | `string` |  |
| `compare_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `blobs_url` | `string` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `role_name` | `string` |  |
| `assignees_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `fork` | `boolean` |  |
| `trees_url` | `string` |  |
| `git_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `license` | `object` |  |
| `notifications_url` | `string` |  |
| `html_url` | `string` |  |
| `statuses_url` | `string` |  |
| `clone_url` | `string` |  |
| `mirror_url` | `string` |  |
| `merges_url` | `string` |  |
| `teams_url` | `string` |  |
| `ssh_url` | `string` |  |
| `releases_url` | `string` |  |
| `disabled` | `boolean` |  |
| `forks_count` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `private` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `comments_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `issues_url` | `string` |  |
| `labels_url` | `string` |  |
| `topics` | `array` |  |
| `homepage` | `string` |  |
| `pushed_at` | `string` |  |
| `language` | `string` |  |
| `url` | `string` |  |
| `downloads_url` | `string` |  |
| `created_at` | `string` |  |
| `network_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `permissions` | `object` |  |
| `forks_url` | `string` |  |
| `updated_at` | `string` |  |
| `git_tags_url` | `string` |  |
| `default_branch` | `string` |  |
| `has_issues` | `boolean` |  |
| `forks` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `archive_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `tags_url` | `string` |  |
| `deployments_url` | `string` |  |
| `svn_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `node_id` | `string` |  |
| `branches_url` | `string` |  |
| `open_issues` | `integer` |  |
| `keys_url` | `string` |  |
| `full_name` | `string` |  |
| `contents_url` | `string` |  |
| `languages_url` | `string` |  |
| `milestones_url` | `string` |  |
| `is_template` | `boolean` |  |
| `visibility` | `string` |  |
| `watchers` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
