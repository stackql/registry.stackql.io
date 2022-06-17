---
title: issues_and_pull_requests
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
<tr><td><b>Name</b></td><td><code>github.search.issues_and_pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.issues_and_pull_requests</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `updated_at` | `string` |  |
| `timeline_url` | `string` |  |
| `user` | `object` | Simple User |
| `number` | `integer` |  |
| `repository` | `object` | A git repository |
| `labels` | `array` |  |
| `assignee` | `object` | Simple User |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `body` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `author_association` | `string` | How the author is associated with the repository. |
| `comments_url` | `string` |  |
| `created_at` | `string` |  |
| `text_matches` | `array` |  |
| `active_lock_reason` | `string` |  |
| `pull_request` | `object` |  |
| `state` | `string` |  |
| `closed_at` | `string` |  |
| `url` | `string` |  |
| `repository_url` | `string` |  |
| `comments` | `integer` |  |
| `assignees` | `array` |  |
| `reactions` | `object` |  |
| `events_url` | `string` |  |
| `body_text` | `string` |  |
| `draft` | `boolean` |  |
| `title` | `string` |  |
| `score` | `number` |  |
| `body_html` | `string` |  |
| `labels_url` | `string` |  |
| `locked` | `boolean` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `issues_and_pull_requests` | `q` | Find issues by state and keyword. This method returns up to 100 results [per page](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination).<br /><br />When searching for issues, you can get text match metadata for the issue **title**, issue **body**, and issue **comment body** fields when you pass the `text-match` media type. For more details about how to receive highlighted<br />search results, see [Text match metadata](https://docs.github.com/rest/reference/search#text-match-metadata).<br /><br />For example, if you want to find the oldest unresolved Python bugs on Windows. Your query might look something like this.<br /><br />`q=windows+label:bug+language:python+state:open&sort=created&order=asc`<br /><br />This query searches for the keyword `windows`, within any open issue that is labeled as `bug`. The search runs across repositories whose primary language is Python. The results are sorted by creation date in ascending order, which means the oldest issues appear first in the search results.<br /><br />**Note:** For [user-to-server](https://docs.github.com/developers/apps/identifying-and-authorizing-users-for-github-apps#user-to-server-requests) GitHub App requests, you can't retrieve a combination of issues and pull requests in a single query. Requests that don't include the `is:issue` or `is:pull-request` qualifier will receive an HTTP `422 Unprocessable Entity` response. To get results for both issues and pull requests, you must send separate queries for issues and pull requests. For more information about the `is` qualifier, see "[Searching only issues or pull requests](https://docs.github.com/github/searching-for-information-on-github/searching-issues-and-pull-requests#search-only-issues-or-pull-requests)." | SELECT |
