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
<tr><td><b>Name</b></td><td><code>github.activity.starred_repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.starred_repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `contributors_url` | `string` |  |
| `mirror_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `watchers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `subscribers_url` | `string` |  |
| `notifications_url` | `string` |  |
| `assignees_url` | `string` |  |
| `starred_at` | `string` |  |
| `git_url` | `string` |  |
| `html_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `watchers` | `integer` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `tags_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `fork` | `boolean` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `language` | `string` |  |
| `pulls_url` | `string` |  |
| `releases_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `hooks_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `node_id` | `string` |  |
| `blobs_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `temp_clone_token` | `string` |  |
| `stargazers_url` | `string` |  |
| `homepage` | `string` |  |
| `master_branch` | `string` |  |
| `subscription_url` | `string` |  |
| `issues_url` | `string` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | Simple User |
| `open_issues` | `integer` |  |
| `svn_url` | `string` |  |
| `teams_url` | `string` |  |
| `labels_url` | `string` |  |
| `deployments_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `permissions` | `object` |  |
| `statuses_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `contents_url` | `string` |  |
| `network_count` | `integer` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `license` | `object` | License Simple |
| `branches_url` | `string` |  |
| `template_repository` | `object` |  |
| `forks_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `size` | `integer` |  |
| `collaborators_url` | `string` |  |
| `trees_url` | `string` |  |
| `clone_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `languages_url` | `string` |  |
| `archive_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `open_issues_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `url` | `string` |  |
| `compare_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `keys_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `created_at` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `git_refs_url` | `string` |  |
| `milestones_url` | `string` |  |
| `topics` | `array` |  |
| `updated_at` | `string` |  |
| `full_name` | `string` |  |
| `organization` | `object` | Simple User |
| `comments_url` | `string` |  |
| `ssh_url` | `string` |  |
| `merges_url` | `string` |  |
| `forks` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_repos_starred_by_authenticated_user` | `` | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: | SELECT |
| `check_repo_is_starred_by_authenticated_user` | `owner, repo` |  | EXEC |
| `list_repos_starred_by_user` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: | EXEC |
| `star_repo_for_authenticated_user` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." | EXEC |
| `unstar_repo_for_authenticated_user` | `owner, repo` |  | EXEC |
