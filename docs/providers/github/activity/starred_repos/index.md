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
| `updated_at` | `string` |  |
| `clone_url` | `string` |  |
| `url` | `string` |  |
| `stargazers_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `archive_url` | `string` |  |
| `svn_url` | `string` |  |
| `notifications_url` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `open_issues` | `integer` |  |
| `forks_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `created_at` | `string` |  |
| `language` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `git_tags_url` | `string` |  |
| `permissions` | `object` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `default_branch` | `string` | The default branch of the repository. |
| `downloads_url` | `string` |  |
| `owner` | `object` | Simple User |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `events_url` | `string` |  |
| `hooks_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `assignees_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `forks` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `statuses_url` | `string` |  |
| `compare_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `starred_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `tags_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `milestones_url` | `string` |  |
| `keys_url` | `string` |  |
| `git_url` | `string` |  |
| `releases_url` | `string` |  |
| `fork` | `boolean` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `mirror_url` | `string` |  |
| `languages_url` | `string` |  |
| `deployments_url` | `string` |  |
| `license` | `object` | License Simple |
| `comments_url` | `string` |  |
| `blobs_url` | `string` |  |
| `contents_url` | `string` |  |
| `merges_url` | `string` |  |
| `full_name` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `size` | `integer` |  |
| `subscribers_url` | `string` |  |
| `commits_url` | `string` |  |
| `topics` | `array` |  |
| `html_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `teams_url` | `string` |  |
| `pulls_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `trees_url` | `string` |  |
| `organization` | `object` | Simple User |
| `homepage` | `string` |  |
| `network_count` | `integer` |  |
| `master_branch` | `string` |  |
| `temp_clone_token` | `string` |  |
| `labels_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `issues_url` | `string` |  |
| `subscription_url` | `string` |  |
| `watchers` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `template_repository` | `object` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `contributors_url` | `string` |  |
| `ssh_url` | `string` |  |
| `branches_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
