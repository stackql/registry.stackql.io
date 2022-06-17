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
| `comments_url` | `string` |  |
| `html_url` | `string` |  |
| `events_url` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `number` | `integer` |  |
| `repository_url` | `string` |  |
| `score` | `number` |  |
| `url` | `string` |  |
| `text_matches` | `array` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `state` | `string` |  |
| `draft` | `boolean` |  |
| `pull_request` | `object` |  |
| `labels_url` | `string` |  |
| `title` | `string` |  |
| `closed_at` | `string` |  |
| `node_id` | `string` |  |
| `body_html` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `assignee` | `object` | Simple User |
| `repository` | `object` | A git repository |
| `body_text` | `string` |  |
| `labels` | `array` |  |
| `body` | `string` |  |
| `timeline_url` | `string` |  |
| `created_at` | `string` |  |
| `assignees` | `array` |  |
| `locked` | `boolean` |  |
| `reactions` | `object` |  |
| `updated_at` | `string` |  |
| `comments` | `integer` |  |
| `active_lock_reason` | `string` |  |
| `user` | `object` | Simple User |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `issues_and_pull_requests` | `SELECT` | `q` |
