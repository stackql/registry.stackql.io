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
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `fingerprint` | `string` |  |
| `org_id` | `integer` |  |
| `events_were` | `array` |  |
| `deploy_key_fingerprint` | `string` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `target_login` | `string` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `team` | `string` |  |
| `active` | `boolean` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `content_type` | `string` |  |
| `hook_id` | `integer` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `read_only` | `boolean` |  |
| `repository_public` | `boolean` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `actor` | `string` | The actor who performed the action. |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `old_user` | `string` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `data` | `object` |  |
| `events` | `array` |  |
| `explanation` | `string` |  |
| `emoji` | `string` |  |
| `business` | `string` |  |
| `repository` | `string` | The name of the repository. |
| `actor_location` | `object` |  |
| `previous_visibility` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `config_was` | `array` |  |
| `limited_availability` | `boolean` |  |
| `active_was` | `boolean` |  |
| `org` | `string` |  |
| `config` | `array` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `message` | `string` |  |
| `openssh_public_key` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `enterprise` |
