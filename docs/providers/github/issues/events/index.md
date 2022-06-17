---
title: events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `requested_reviewer` | `object` | Simple User |
| `dismissed_review` | `object` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `lock_reason` | `string` |  |
| `assigner` | `object` | Simple User |
| `node_id` | `string` |  |
| `review_requester` | `object` | Simple User |
| `project_card` | `object` | Issue Event Project Card |
| `assignee` | `object` | Simple User |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `rename` | `object` | Issue Event Rename |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestone` | `object` | Issue Event Milestone |
| `commit_url` | `string` |  |
| `label` | `object` | Issue Event Label |
| `actor` | `object` | Simple User |
| `event` | `string` |  |
| `commit_id` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_event` | `SELECT` | `event_id, owner, repo` |
| `list_events_for_repo` | `SELECT` | `owner, repo` |
