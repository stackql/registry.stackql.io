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
| `actor` | `string` | The actor who performed the action. |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `events` | `array` |  |
| `active` | `boolean` |  |
| `config_was` | `array` |  |
| `target_login` | `string` |  |
| `repository_public` | `boolean` |  |
| `active_was` | `boolean` |  |
| `deploy_key_fingerprint` | `string` |  |
| `org` | `string` |  |
| `team` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `old_user` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `data` | `object` |  |
| `hook_id` | `integer` |  |
| `emoji` | `string` |  |
| `limited_availability` | `boolean` |  |
| `events_were` | `array` |  |
| `read_only` | `boolean` |  |
| `business` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `actor_location` | `object` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `previous_visibility` | `string` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `content_type` | `string` |  |
| `org_id` | `integer` |  |
| `config` | `array` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `message` | `string` |  |
| `repository` | `string` | The name of the repository. |
| `explanation` | `string` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `openssh_public_key` | `string` |  |
| `fingerprint` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `enterprise` |
