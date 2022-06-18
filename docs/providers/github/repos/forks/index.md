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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.forks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `merges_url` | `string` |  |
| `is_template` | `boolean` |  |
| `issues_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `tags_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `forks_url` | `string` |  |
| `blobs_url` | `string` |  |
| `downloads_url` | `string` |  |
| `owner` | `object` | Simple User |
| `temp_clone_token` | `string` |  |
| `open_issues` | `integer` |  |
| `network_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `private` | `boolean` |  |
| `pulls_url` | `string` |  |
| `topics` | `array` |  |
| `size` | `integer` |  |
| `archived` | `boolean` |  |
| `permissions` | `object` |  |
| `archive_url` | `string` |  |
| `milestones_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `clone_url` | `string` |  |
| `teams_url` | `string` |  |
| `hooks_url` | `string` |  |
| `visibility` | `string` |  |
| `compare_url` | `string` |  |
| `assignees_url` | `string` |  |
| `role_name` | `string` |  |
| `license` | `object` |  |
| `full_name` | `string` |  |
| `languages_url` | `string` |  |
| `releases_url` | `string` |  |
| `contributors_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `labels_url` | `string` |  |
| `html_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `mirror_url` | `string` |  |
| `forks_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `svn_url` | `string` |  |
| `git_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `issue_comment_url` | `string` |  |
| `statuses_url` | `string` |  |
| `keys_url` | `string` |  |
| `ssh_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `branches_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `subscription_url` | `string` |  |
| `trees_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `default_branch` | `string` |  |
| `has_issues` | `boolean` |  |
| `pushed_at` | `string` |  |
| `subscribers_count` | `integer` |  |
| `contents_url` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `disabled` | `boolean` |  |
| `homepage` | `string` |  |
| `watchers` | `integer` |  |
| `forks` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `fork` | `boolean` |  |
| `notifications_url` | `string` |  |
| `language` | `string` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
