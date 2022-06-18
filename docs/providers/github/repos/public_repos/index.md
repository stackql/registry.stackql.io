---
title: public_repos
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
<tr><td><b>Name</b></td><td><code>public_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.public_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `releases_url` | `string` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `subscribers_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `subscription_url` | `string` |  |
| `compare_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `disabled` | `boolean` |  |
| `deployments_url` | `string` |  |
| `watchers` | `integer` |  |
| `milestones_url` | `string` |  |
| `html_url` | `string` |  |
| `license` | `object` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `forks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `tags_url` | `string` |  |
| `downloads_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `language` | `string` |  |
| `archive_url` | `string` |  |
| `permissions` | `object` |  |
| `archived` | `boolean` |  |
| `updated_at` | `string` |  |
| `is_template` | `boolean` |  |
| `contents_url` | `string` |  |
| `default_branch` | `string` |  |
| `network_count` | `integer` |  |
| `notifications_url` | `string` |  |
| `labels_url` | `string` |  |
| `git_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `visibility` | `string` |  |
| `watchers_count` | `integer` |  |
| `homepage` | `string` |  |
| `commits_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `forks` | `integer` |  |
| `git_refs_url` | `string` |  |
| `fork` | `boolean` |  |
| `url` | `string` |  |
| `branches_url` | `string` |  |
| `owner` | `object` | Simple User |
| `clone_url` | `string` |  |
| `forks_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `statuses_url` | `string` |  |
| `open_issues` | `integer` |  |
| `topics` | `array` |  |
| `full_name` | `string` |  |
| `mirror_url` | `string` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `merges_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `events_url` | `string` |  |
| `languages_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `issues_url` | `string` |  |
| `blobs_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `pulls_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `pushed_at` | `string` |  |
| `private` | `boolean` |  |
| `teams_url` | `string` |  |
| `contributors_url` | `string` |  |
| `assignees_url` | `string` |  |
| `size` | `integer` |  |
| `keys_url` | `string` |  |
| `comments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `ssh_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `template_repository` | `object` | A git repository |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
