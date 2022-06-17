---
title: contributors
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
<tr><td><b>Name</b></td><td><code>github.repos.contributors</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.contributors</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `gravatar_id` | `string` |  |
| `followers_url` | `string` |  |
| `repos_url` | `string` |  |
| `email` | `string` |  |
| `gists_url` | `string` |  |
| `node_id` | `string` |  |
| `subscriptions_url` | `string` |  |
| `login` | `string` |  |
| `received_events_url` | `string` |  |
| `starred_url` | `string` |  |
| `site_admin` | `boolean` |  |
| `html_url` | `string` |  |
| `events_url` | `string` |  |
| `organizations_url` | `string` |  |
| `following_url` | `string` |  |
| `avatar_url` | `string` |  |
| `contributions` | `integer` |  |
| `url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_contributors` | `owner, repo` | Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API v3 caches contributor data to improve performance.<br /><br />GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information. | SELECT |
