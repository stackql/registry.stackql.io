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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `url` | `string` |  |
| `dismissed_review` | `object` |  |
| `actor` | `object` | Simple User |
| `node_id` | `string` |  |
| `lock_reason` | `string` |  |
| `requested_reviewer` | `object` | Simple User |
| `label` | `object` | Issue Event Label |
| `project_card` | `object` | Issue Event Project Card |
| `event` | `string` |  |
| `assignee` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `assigner` | `object` | Simple User |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `created_at` | `string` |  |
| `commit_url` | `string` |  |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `rename` | `object` | Issue Event Rename |
| `review_requester` | `object` | Simple User |
| `milestone` | `object` | Issue Event Milestone |
| `commit_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_event` | `SELECT` | `event_id, owner, repo` |
| `list_events_for_repo` | `SELECT` | `owner, repo` |
