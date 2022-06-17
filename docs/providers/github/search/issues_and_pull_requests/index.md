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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>issues_and_pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.issues_and_pull_requests</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `locked` | `boolean` |  |
| `text_matches` | `array` |  |
| `labels` | `array` |  |
| `closed_at` | `string` |  |
| `assignee` | `object` | Simple User |
| `events_url` | `string` |  |
| `labels_url` | `string` |  |
| `score` | `number` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `node_id` | `string` |  |
| `repository` | `object` | A git repository |
| `html_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `user` | `object` | Simple User |
| `title` | `string` |  |
| `state` | `string` |  |
| `updated_at` | `string` |  |
| `draft` | `boolean` |  |
| `comments_url` | `string` |  |
| `comments` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `created_at` | `string` |  |
| `body_html` | `string` |  |
| `timeline_url` | `string` |  |
| `repository_url` | `string` |  |
| `number` | `integer` |  |
| `body_text` | `string` |  |
| `reactions` | `object` |  |
| `assignees` | `array` |  |
| `pull_request` | `object` |  |
| `url` | `string` |  |
| `body` | `string` |  |
## Methods
