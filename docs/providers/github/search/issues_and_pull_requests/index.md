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
<tr><td><b>Name</b></td><td><code>issues_and_pull_requests</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.issues_and_pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `events_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `labels_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `updated_at` | `string` |  |
| `text_matches` | `array` |  |
| `node_id` | `string` |  |
| `title` | `string` |  |
| `body` | `string` |  |
| `score` | `number` |  |
| `labels` | `array` |  |
| `number` | `integer` |  |
| `body_text` | `string` |  |
| `body_html` | `string` |  |
| `comments_url` | `string` |  |
| `assignees` | `array` |  |
| `created_at` | `string` |  |
| `repository_url` | `string` |  |
| `closed_at` | `string` |  |
| `active_lock_reason` | `string` |  |
| `draft` | `boolean` |  |
| `url` | `string` |  |
| `pull_request` | `object` |  |
| `locked` | `boolean` |  |
| `repository` | `object` | A git repository |
| `assignee` | `object` | Simple User |
| `state` | `string` |  |
| `user` | `object` | Simple User |
| `timeline_url` | `string` |  |
| `comments` | `integer` |  |
| `reactions` | `object` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `issues_and_pull_requests` | `SELECT` | `q` |
