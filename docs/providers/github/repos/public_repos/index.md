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
| `collaborators_url` | `string` |  |
| `updated_at` | `string` |  |
| `forks` | `integer` |  |
| `issue_events_url` | `string` |  |
| `keys_url` | `string` |  |
| `merges_url` | `string` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `archive_url` | `string` |  |
| `assignees_url` | `string` |  |
| `network_count` | `integer` |  |
| `html_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `watchers` | `integer` |  |
| `homepage` | `string` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_pages` | `boolean` |  |
| `trees_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `node_id` | `string` |  |
| `subscription_url` | `string` |  |
| `svn_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `private` | `boolean` |  |
| `releases_url` | `string` |  |
| `languages_url` | `string` |  |
| `pulls_url` | `string` |  |
| `created_at` | `string` |  |
| `open_issues` | `integer` |  |
| `clone_url` | `string` |  |
| `branches_url` | `string` |  |
| `commits_url` | `string` |  |
| `statuses_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `default_branch` | `string` |  |
| `has_wiki` | `boolean` |  |
| `size` | `integer` |  |
| `forks_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `is_template` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `full_name` | `string` |  |
| `role_name` | `string` |  |
| `compare_url` | `string` |  |
| `license` | `object` |  |
| `url` | `string` |  |
| `issues_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `disabled` | `boolean` |  |
| `downloads_url` | `string` |  |
| `fork` | `boolean` |  |
| `owner` | `object` | Simple User |
| `tags_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `contents_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `teams_url` | `string` |  |
| `notifications_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `visibility` | `string` |  |
| `temp_clone_token` | `string` |  |
| `blobs_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `archived` | `boolean` |  |
| `git_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `language` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `mirror_url` | `string` |  |
| `permissions` | `object` |  |
| `labels_url` | `string` |  |
| `deployments_url` | `string` |  |
| `contributors_url` | `string` |  |
| `topics` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
