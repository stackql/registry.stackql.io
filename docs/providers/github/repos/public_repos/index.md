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
| `language` | `string` |  |
| `languages_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `git_url` | `string` |  |
| `teams_url` | `string` |  |
| `updated_at` | `string` |  |
| `watchers` | `integer` |  |
| `clone_url` | `string` |  |
| `merges_url` | `string` |  |
| `pushed_at` | `string` |  |
| `deployments_url` | `string` |  |
| `downloads_url` | `string` |  |
| `branches_url` | `string` |  |
| `comments_url` | `string` |  |
| `default_branch` | `string` |  |
| `temp_clone_token` | `string` |  |
| `ssh_url` | `string` |  |
| `license` | `object` |  |
| `open_issues_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `disabled` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `blobs_url` | `string` |  |
| `topics` | `array` |  |
| `size` | `integer` |  |
| `network_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `role_name` | `string` |  |
| `hooks_url` | `string` |  |
| `notifications_url` | `string` |  |
| `archive_url` | `string` |  |
| `releases_url` | `string` |  |
| `forks_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `permissions` | `object` |  |
| `open_issues` | `integer` |  |
| `labels_url` | `string` |  |
| `created_at` | `string` |  |
| `forks_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `is_template` | `boolean` |  |
| `tags_url` | `string` |  |
| `assignees_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `forks` | `integer` |  |
| `private` | `boolean` |  |
| `pulls_url` | `string` |  |
| `mirror_url` | `string` |  |
| `visibility` | `string` |  |
| `owner` | `object` | Simple User |
| `has_wiki` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `trees_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `homepage` | `string` |  |
| `subscribers_url` | `string` |  |
| `issues_url` | `string` |  |
| `html_url` | `string` |  |
| `fork` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `git_refs_url` | `string` |  |
| `compare_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `keys_url` | `string` |  |
| `archived` | `boolean` |  |
| `contents_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_downloads` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `contributors_url` | `string` |  |
| `milestones_url` | `string` |  |
| `node_id` | `string` |  |
| `svn_url` | `string` |  |
| `url` | `string` |  |
| `full_name` | `string` |  |
| `watchers_count` | `integer` |  |
| `statuses_url` | `string` |  |
| `issue_events_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
