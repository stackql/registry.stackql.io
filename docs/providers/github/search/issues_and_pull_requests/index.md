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
| `score` | `number` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `comments_url` | `string` |  |
| `repository` | `object` | A git repository |
| `labels_url` | `string` |  |
| `comments` | `integer` |  |
| `reactions` | `object` |  |
| `body` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `active_lock_reason` | `string` |  |
| `closed_at` | `string` |  |
| `timeline_url` | `string` |  |
| `number` | `integer` |  |
| `text_matches` | `array` |  |
| `assignee` | `object` | Simple User |
| `assignees` | `array` |  |
| `state` | `string` |  |
| `user` | `object` | Simple User |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `title` | `string` |  |
| `events_url` | `string` |  |
| `pull_request` | `object` |  |
| `labels` | `array` |  |
| `html_url` | `string` |  |
| `body_html` | `string` |  |
| `draft` | `boolean` |  |
| `repository_url` | `string` |  |
| `locked` | `boolean` |  |
| `body_text` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `issues_and_pull_requests` | `SELECT` | `q` |
