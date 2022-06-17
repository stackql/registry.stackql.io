---
title: issues
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
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.issues</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `node_id` | `string` |  |
| `repository_url` | `string` |  |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `repository` | `object` | A git repository |
| `active_lock_reason` | `string` |  |
| `draft` | `boolean` |  |
| `updated_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `body_html` | `string` |  |
| `comments_url` | `string` |  |
| `title` | `string` | Title of the issue |
| `body_text` | `string` |  |
| `closed_at` | `string` |  |
| `html_url` | `string` |  |
| `timeline_url` | `string` |  |
| `body` | `string` | Contents of the issue |
| `locked` | `boolean` |  |
| `assignee` | `object` | Simple User |
| `labels_url` | `string` |  |
| `events_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assignees` | `array` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `comments` | `integer` |  |
| `user` | `object` | Simple User |
| `closed_by` | `object` | Simple User |
| `reactions` | `object` |  |
| `pull_request` | `object` |  |
| `url` | `string` | URL for the issue |
| `created_at` | `string` |  |
## Methods
