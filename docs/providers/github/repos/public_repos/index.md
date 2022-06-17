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
<tr><td><b>Name</b></td><td><code>github.repos.public_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.public_repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `homepage` | `string` |  |
| `fork` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `size` | `integer` |  |
| `created_at` | `string` |  |
| `merges_url` | `string` |  |
| `updated_at` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `is_template` | `boolean` |  |
| `assignees_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `ssh_url` | `string` |  |
| `compare_url` | `string` |  |
| `url` | `string` |  |
| `topics` | `array` |  |
| `branches_url` | `string` |  |
| `events_url` | `string` |  |
| `comments_url` | `string` |  |
| `role_name` | `string` |  |
| `blobs_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `languages_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `git_commits_url` | `string` |  |
| `visibility` | `string` |  |
| `disabled` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `releases_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `forks` | `integer` |  |
| `downloads_url` | `string` |  |
| `network_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `archived` | `boolean` |  |
| `deployments_url` | `string` |  |
| `full_name` | `string` |  |
| `forks_url` | `string` |  |
| `mirror_url` | `string` |  |
| `pulls_url` | `string` |  |
| `contents_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `watchers` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `labels_url` | `string` |  |
| `license` | `object` |  |
| `permissions` | `object` |  |
| `owner` | `object` | Simple User |
| `archive_url` | `string` |  |
| `html_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `commits_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `issues_url` | `string` |  |
| `clone_url` | `string` |  |
| `teams_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `open_issues` | `integer` |  |
| `watchers_count` | `integer` |  |
| `trees_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `forks_count` | `integer` |  |
| `node_id` | `string` |  |
| `contributors_url` | `string` |  |
| `tags_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `hooks_url` | `string` |  |
| `svn_url` | `string` |  |
| `default_branch` | `string` |  |
| `pushed_at` | `string` |  |
| `keys_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `language` | `string` |  |
| `private` | `boolean` |  |
| `notifications_url` | `string` |  |
| `subscription_url` | `string` |  |
| `has_issues` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_public` | `` | Lists all public repositories in the order that they were created.<br /><br />Note:<br />- For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise.<br />- Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of repositories. | SELECT |
