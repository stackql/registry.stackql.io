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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.public_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `trees_url` | `string` |  |
| `assignees_url` | `string` |  |
| `disabled` | `boolean` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `milestones_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `default_branch` | `string` |  |
| `forks_count` | `integer` |  |
| `git_url` | `string` |  |
| `contributors_url` | `string` |  |
| `merges_url` | `string` |  |
| `topics` | `array` |  |
| `network_count` | `integer` |  |
| `events_url` | `string` |  |
| `is_template` | `boolean` |  |
| `visibility` | `string` |  |
| `owner` | `object` | Simple User |
| `clone_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `languages_url` | `string` |  |
| `private` | `boolean` |  |
| `pulls_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `branches_url` | `string` |  |
| `teams_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `deployments_url` | `string` |  |
| `forks_url` | `string` |  |
| `statuses_url` | `string` |  |
| `tags_url` | `string` |  |
| `keys_url` | `string` |  |
| `archive_url` | `string` |  |
| `mirror_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `ssh_url` | `string` |  |
| `full_name` | `string` |  |
| `language` | `string` |  |
| `notifications_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `archived` | `boolean` |  |
| `created_at` | `string` |  |
| `allow_forking` | `boolean` |  |
| `pushed_at` | `string` |  |
| `has_wiki` | `boolean` |  |
| `homepage` | `string` |  |
| `html_url` | `string` |  |
| `issues_url` | `string` |  |
| `subscription_url` | `string` |  |
| `releases_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `fork` | `boolean` |  |
| `permissions` | `object` |  |
| `has_downloads` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `updated_at` | `string` |  |
| `license` | `object` |  |
| `template_repository` | `object` | A git repository |
| `contents_url` | `string` |  |
| `labels_url` | `string` |  |
| `role_name` | `string` |  |
| `svn_url` | `string` |  |
| `open_issues` | `integer` |  |
| `issue_events_url` | `string` |  |
| `watchers` | `integer` |  |
| `size` | `integer` |  |
| `collaborators_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `comments_url` | `string` |  |
| `forks` | `integer` |  |
| `commits_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `downloads_url` | `string` |  |
| `hooks_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `compare_url` | `string` |  |
| `subscribers_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
