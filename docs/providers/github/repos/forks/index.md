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
<tr><td><b>Name</b></td><td><code>github.repos.forks</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.forks</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `allow_forking` | `boolean` |  |
| `events_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `license` | `object` |  |
| `commits_url` | `string` |  |
| `default_branch` | `string` |  |
| `pulls_url` | `string` |  |
| `watchers` | `integer` |  |
| `git_url` | `string` |  |
| `forks_url` | `string` |  |
| `role_name` | `string` |  |
| `url` | `string` |  |
| `forks_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `milestones_url` | `string` |  |
| `comments_url` | `string` |  |
| `mirror_url` | `string` |  |
| `ssh_url` | `string` |  |
| `permissions` | `object` |  |
| `git_commits_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `visibility` | `string` |  |
| `teams_url` | `string` |  |
| `contents_url` | `string` |  |
| `releases_url` | `string` |  |
| `open_issues` | `integer` |  |
| `topics` | `array` |  |
| `size` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `owner` | `object` | Simple User |
| `has_projects` | `boolean` |  |
| `languages_url` | `string` |  |
| `blobs_url` | `string` |  |
| `archive_url` | `string` |  |
| `fork` | `boolean` |  |
| `created_at` | `string` |  |
| `language` | `string` |  |
| `pushed_at` | `string` |  |
| `compare_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `assignees_url` | `string` |  |
| `homepage` | `string` |  |
| `labels_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `trees_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `archived` | `boolean` |  |
| `deployments_url` | `string` |  |
| `branches_url` | `string` |  |
| `keys_url` | `string` |  |
| `svn_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `network_count` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `statuses_url` | `string` |  |
| `notifications_url` | `string` |  |
| `full_name` | `string` |  |
| `private` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `hooks_url` | `string` |  |
| `issues_url` | `string` |  |
| `html_url` | `string` |  |
| `downloads_url` | `string` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `disabled` | `boolean` |  |
| `merges_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `forks` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `subscription_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `clone_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_forks` | `owner, repo` |  | SELECT |
| `create_fork` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). | INSERT |
