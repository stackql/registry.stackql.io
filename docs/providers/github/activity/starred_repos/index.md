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
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `network_count` | `integer` |  |
| `svn_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `size` | `integer` |  |
| `collaborators_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `comments_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `contents_url` | `string` |  |
| `updated_at` | `string` |  |
| `ssh_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `issues_url` | `string` |  |
| `contributors_url` | `string` |  |
| `topics` | `array` |  |
| `homepage` | `string` |  |
| `trees_url` | `string` |  |
| `statuses_url` | `string` |  |
| `deployments_url` | `string` |  |
| `tags_url` | `string` |  |
| `compare_url` | `string` |  |
| `hooks_url` | `string` |  |
| `forks_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `owner` | `object` | Simple User |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `issue_comment_url` | `string` |  |
| `mirror_url` | `string` |  |
| `fork` | `boolean` |  |
| `merges_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `branches_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `commits_url` | `string` |  |
| `forks_count` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `assignees_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `starred_at` | `string` |  |
| `forks` | `integer` |  |
| `master_branch` | `string` |  |
| `notifications_url` | `string` |  |
| `blobs_url` | `string` |  |
| `organization` | `object` | Simple User |
| `subscription_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `releases_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `clone_url` | `string` |  |
| `created_at` | `string` |  |
| `labels_url` | `string` |  |
| `html_url` | `string` |  |
| `template_repository` | `object` |  |
| `license` | `object` | License Simple |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `events_url` | `string` |  |
| `keys_url` | `string` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `stargazers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `language` | `string` |  |
| `git_tags_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `full_name` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `languages_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `permissions` | `object` |  |
| `teams_url` | `string` |  |
| `archive_url` | `string` |  |
| `pulls_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `watchers` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `git_url` | `string` |  |
| `open_issues` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
