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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>starred_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.starred_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `deployments_url` | `string` |  |
| `network_count` | `integer` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `tags_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `html_url` | `string` |  |
| `compare_url` | `string` |  |
| `url` | `string` |  |
| `milestones_url` | `string` |  |
| `forks_url` | `string` |  |
| `hooks_url` | `string` |  |
| `pushed_at` | `string` |  |
| `stargazers_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `owner` | `object` | Simple User |
| `svn_url` | `string` |  |
| `template_repository` | `object` |  |
| `ssh_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `git_commits_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `trees_url` | `string` |  |
| `forks` | `integer` |  |
| `commits_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `watchers_count` | `integer` |  |
| `branches_url` | `string` |  |
| `downloads_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `events_url` | `string` |  |
| `watchers` | `integer` |  |
| `clone_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `archive_url` | `string` |  |
| `updated_at` | `string` |  |
| `subscribers_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `topics` | `array` |  |
| `language` | `string` |  |
| `labels_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `fork` | `boolean` |  |
| `forks_count` | `integer` |  |
| `git_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `teams_url` | `string` |  |
| `contributors_url` | `string` |  |
| `assignees_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `permissions` | `object` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `temp_clone_token` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `subscribers_url` | `string` |  |
| `subscription_url` | `string` |  |
| `license` | `object` | License Simple |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `has_pages` | `boolean` |  |
| `homepage` | `string` |  |
| `merges_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `blobs_url` | `string` |  |
| `keys_url` | `string` |  |
| `full_name` | `string` |  |
| `git_refs_url` | `string` |  |
| `contents_url` | `string` |  |
| `size` | `integer` |  |
| `issue_events_url` | `string` |  |
| `open_issues` | `integer` |  |
| `issues_url` | `string` |  |
| `releases_url` | `string` |  |
| `languages_url` | `string` |  |
| `starred_at` | `string` |  |
| `comments_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `statuses_url` | `string` |  |
| `pulls_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `notifications_url` | `string` |  |
| `organization` | `object` | Simple User |
| `master_branch` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
