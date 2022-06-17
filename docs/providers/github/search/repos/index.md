---
title: repos
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
<tr><td><b>Name</b></td><td><code>github.search.repos</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.repos</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `fork` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `topics` | `array` |  |
| `full_name` | `string` |  |
| `archive_url` | `string` |  |
| `owner` | `object` | Simple User |
| `issue_comment_url` | `string` |  |
| `archived` | `boolean` |  |
| `node_id` | `string` |  |
| `events_url` | `string` |  |
| `statuses_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `tags_url` | `string` |  |
| `milestones_url` | `string` |  |
| `downloads_url` | `string` |  |
| `hooks_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `subscription_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `homepage` | `string` |  |
| `git_tags_url` | `string` |  |
| `commits_url` | `string` |  |
| `forks_count` | `integer` |  |
| `allow_rebase_merge` | `boolean` |  |
| `created_at` | `string` |  |
| `stargazers_url` | `string` |  |
| `score` | `number` |  |
| `clone_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `comments_url` | `string` |  |
| `teams_url` | `string` |  |
| `git_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `text_matches` | `array` |  |
| `ssh_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `html_url` | `string` |  |
| `language` | `string` |  |
| `allow_forking` | `boolean` |  |
| `pulls_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `merges_url` | `string` |  |
| `svn_url` | `string` |  |
| `url` | `string` |  |
| `permissions` | `object` |  |
| `master_branch` | `string` |  |
| `contributors_url` | `string` |  |
| `contents_url` | `string` |  |
| `assignees_url` | `string` |  |
| `private` | `boolean` |  |
| `trees_url` | `string` |  |
| `languages_url` | `string` |  |
| `updated_at` | `string` |  |
| `labels_url` | `string` |  |
| `keys_url` | `string` |  |
| `is_template` | `boolean` |  |
| `open_issues` | `integer` |  |
| `allow_auto_merge` | `boolean` |  |
| `notifications_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `issues_url` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `mirror_url` | `string` |  |
| `watchers` | `integer` |  |
| `releases_url` | `string` |  |
| `compare_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `pushed_at` | `string` |  |
| `forks` | `integer` |  |
| `default_branch` | `string` |  |
| `has_downloads` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `deployments_url` | `string` |  |
| `size` | `integer` |  |
| `branches_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `license` | `object` | License Simple |
| `forks_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `repos` | `q` | Find repositories via various criteria. This method returns up to 100 results [per page](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination).<br /><br />When searching for repositories, you can get text match metadata for the **name** and **description** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/rest/reference/search#text-match-metadata).<br /><br />For example, if you want to search for popular Tetris repositories written in assembly code, your query might look like this:<br /><br />`q=tetris+language:assembly&sort=stars&order=desc`<br /><br />This query searches for repositories with the word `tetris` in the name, the description, or the README. The results are limited to repositories where the primary language is assembly. The results are sorted by stars in descending order, so that the most popular repositories appear first in the search results. | SELECT |
