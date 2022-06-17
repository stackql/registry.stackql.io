---
title: starred_repos
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>starred_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.starred_repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `deployments_url` | `string` |  |
| `topics` | `array` |  |
| `has_pages` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `svn_url` | `string` |  |
| `full_name` | `string` |  |
| `url` | `string` |  |
| `teams_url` | `string` |  |
| `releases_url` | `string` |  |
| `html_url` | `string` |  |
| `ssh_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `commits_url` | `string` |  |
| `issues_url` | `string` |  |
| `git_url` | `string` |  |
| `milestones_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `keys_url` | `string` |  |
| `subscription_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `fork` | `boolean` |  |
| `open_issues` | `integer` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `stargazers_url` | `string` |  |
| `language` | `string` |  |
| `blobs_url` | `string` |  |
| `hooks_url` | `string` |  |
| `forks` | `integer` |  |
| `created_at` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `labels_url` | `string` |  |
| `contributors_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `assignees_url` | `string` |  |
| `starred_at` | `string` |  |
| `node_id` | `string` |  |
| `size` | `integer` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `git_tags_url` | `string` |  |
| `contents_url` | `string` |  |
| `watchers` | `integer` |  |
| `template_repository` | `object` |  |
| `master_branch` | `string` |  |
| `issue_events_url` | `string` |  |
| `compare_url` | `string` |  |
| `license` | `object` | License Simple |
| `issue_comment_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `subscribers_url` | `string` |  |
| `homepage` | `string` |  |
| `temp_clone_token` | `string` |  |
| `branches_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `notifications_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `merges_url` | `string` |  |
| `trees_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `pushed_at` | `string` |  |
| `git_refs_url` | `string` |  |
| `network_count` | `integer` |  |
| `permissions` | `object` |  |
| `clone_url` | `string` |  |
| `updated_at` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `comments_url` | `string` |  |
| `forks_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `archive_url` | `string` |  |
| `tags_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `statuses_url` | `string` |  |
| `pulls_url` | `string` |  |
| `languages_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `private` | `boolean` | Whether the repository is private or public. |
| `default_branch` | `string` | The default branch of the repository. |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `forks_url` | `string` |  |
| `owner` | `object` | Simple User |
| `organization` | `object` | Simple User |
| `events_url` | `string` |  |
## Methods
