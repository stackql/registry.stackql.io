---
title: audit_log_events
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
<tr><td><b>Name</b></td><td><code>audit_log_events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `actor_location` | `object` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `blocked_user` | `string` | The username of the account being blocked. |
| `repo` | `string` | The name of the repository. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `hook_id` | `integer` |  |
| `deploy_key_fingerprint` | `string` |  |
| `active_was` | `boolean` |  |
| `fingerprint` | `string` |  |
| `explanation` | `string` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `emoji` | `string` |  |
| `content_type` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `old_user` | `string` |  |
| `config` | `array` |  |
| `active` | `boolean` |  |
| `events_were` | `array` |  |
| `target_login` | `string` |  |
| `repository` | `string` | The name of the repository. |
| `actor` | `string` | The actor who performed the action. |
| `org_id` | `integer` |  |
| `previous_visibility` | `string` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `team` | `string` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `org` | `string` |  |
| `openssh_public_key` | `string` |  |
| `read_only` | `boolean` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `events` | `array` |  |
| `config_was` | `array` |  |
| `message` | `string` |  |
| `data` | `object` |  |
| `business` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `limited_availability` | `boolean` |  |
| `repository_public` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `org` |
