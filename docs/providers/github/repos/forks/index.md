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
| `url` | `string` |  |
| `events_url` | `string` |  |
| `node_id` | `string` |  |
| `has_pages` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `role_name` | `string` |  |
| `downloads_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `mirror_url` | `string` |  |
| `forks_url` | `string` |  |
| `topics` | `array` |  |
| `contributors_url` | `string` |  |
| `forks` | `integer` |  |
| `languages_url` | `string` |  |
| `language` | `string` |  |
| `hooks_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `branches_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `archived` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `issues_url` | `string` |  |
| `private` | `boolean` |  |
| `pushed_at` | `string` |  |
| `merges_url` | `string` |  |
| `clone_url` | `string` |  |
| `html_url` | `string` |  |
| `open_issues` | `integer` |  |
| `size` | `integer` |  |
| `stargazers_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `notifications_url` | `string` |  |
| `statuses_url` | `string` |  |
| `disabled` | `boolean` |  |
| `releases_url` | `string` |  |
| `watchers` | `integer` |  |
| `forks_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `deployments_url` | `string` |  |
| `updated_at` | `string` |  |
| `contents_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `fork` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `subscribers_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `keys_url` | `string` |  |
| `labels_url` | `string` |  |
| `permissions` | `object` |  |
| `has_issues` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `archive_url` | `string` |  |
| `pulls_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `created_at` | `string` |  |
| `license` | `object` |  |
| `watchers_count` | `integer` |  |
| `owner` | `object` | Simple User |
| `ssh_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `git_url` | `string` |  |
| `default_branch` | `string` |  |
| `subscription_url` | `string` |  |
| `commits_url` | `string` |  |
| `tags_url` | `string` |  |
| `comments_url` | `string` |  |
| `homepage` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `full_name` | `string` |  |
| `blobs_url` | `string` |  |
| `visibility` | `string` |  |
| `network_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `teams_url` | `string` |  |
| `svn_url` | `string` |  |
| `milestones_url` | `string` |  |
| `trees_url` | `string` |  |
| `compare_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
