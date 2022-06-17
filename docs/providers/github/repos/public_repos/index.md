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
| `node_id` | `string` |  |
| `has_projects` | `boolean` |  |
| `created_at` | `string` |  |
| `size` | `integer` |  |
| `git_tags_url` | `string` |  |
| `pushed_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `keys_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `allow_forking` | `boolean` |  |
| `hooks_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `topics` | `array` |  |
| `milestones_url` | `string` |  |
| `events_url` | `string` |  |
| `subscription_url` | `string` |  |
| `downloads_url` | `string` |  |
| `visibility` | `string` |  |
| `url` | `string` |  |
| `forks_count` | `integer` |  |
| `html_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `merges_url` | `string` |  |
| `comments_url` | `string` |  |
| `git_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `mirror_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `issues_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `homepage` | `string` |  |
| `deployments_url` | `string` |  |
| `contributors_url` | `string` |  |
| `commits_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `permissions` | `object` |  |
| `contents_url` | `string` |  |
| `languages_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `network_count` | `integer` |  |
| `archive_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `default_branch` | `string` |  |
| `language` | `string` |  |
| `notifications_url` | `string` |  |
| `tags_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `license` | `object` |  |
| `ssh_url` | `string` |  |
| `compare_url` | `string` |  |
| `disabled` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `statuses_url` | `string` |  |
| `forks` | `integer` |  |
| `watchers` | `integer` |  |
| `is_template` | `boolean` |  |
| `fork` | `boolean` |  |
| `archived` | `boolean` |  |
| `private` | `boolean` |  |
| `trees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `labels_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `assignees_url` | `string` |  |
| `teams_url` | `string` |  |
| `branches_url` | `string` |  |
| `full_name` | `string` |  |
| `updated_at` | `string` |  |
| `role_name` | `string` |  |
| `forks_url` | `string` |  |
| `releases_url` | `string` |  |
| `svn_url` | `string` |  |
| `owner` | `object` | Simple User |
| `clone_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_pages` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
