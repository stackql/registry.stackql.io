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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.starred_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `stargazers_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `merges_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `template_repository` | `object` |  |
| `topics` | `array` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `comments_url` | `string` |  |
| `keys_url` | `string` |  |
| `teams_url` | `string` |  |
| `trees_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `releases_url` | `string` |  |
| `fork` | `boolean` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `languages_url` | `string` |  |
| `milestones_url` | `string` |  |
| `license` | `object` | License Simple |
| `issue_comment_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `open_issues_count` | `integer` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `subscribers_count` | `integer` |  |
| `updated_at` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `commits_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `mirror_url` | `string` |  |
| `subscription_url` | `string` |  |
| `open_issues` | `integer` |  |
| `issues_url` | `string` |  |
| `notifications_url` | `string` |  |
| `network_count` | `integer` |  |
| `owner` | `object` | Simple User |
| `blobs_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `git_url` | `string` |  |
| `full_name` | `string` |  |
| `compare_url` | `string` |  |
| `homepage` | `string` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `deployments_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `clone_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `branches_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `html_url` | `string` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `git_refs_url` | `string` |  |
| `hooks_url` | `string` |  |
| `pushed_at` | `string` |  |
| `master_branch` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `git_tags_url` | `string` |  |
| `ssh_url` | `string` |  |
| `pulls_url` | `string` |  |
| `svn_url` | `string` |  |
| `statuses_url` | `string` |  |
| `organization` | `object` | Simple User |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `archive_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `downloads_url` | `string` |  |
| `assignees_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `language` | `string` |  |
| `forks` | `integer` |  |
| `permissions` | `object` |  |
| `contents_url` | `string` |  |
| `starred_at` | `string` |  |
| `watchers` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `labels_url` | `string` |  |
| `size` | `integer` |  |
| `contributors_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
