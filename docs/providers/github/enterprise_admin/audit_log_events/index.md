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
| `_document_id` | `string` | A unique identifier for an audit event. |
| `openssh_public_key` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `fingerprint` | `string` |  |
| `explanation` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `emoji` | `string` |  |
| `config_was` | `array` |  |
| `repository` | `string` | The name of the repository. |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `repository_public` | `boolean` |  |
| `active_was` | `boolean` |  |
| `actor_location` | `object` |  |
| `active` | `boolean` |  |
| `hook_id` | `integer` |  |
| `team` | `string` |  |
| `deploy_key_fingerprint` | `string` |  |
| `old_user` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `message` | `string` |  |
| `read_only` | `boolean` |  |
| `org` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `blocked_user` | `string` | The username of the account being blocked. |
| `config` | `array` |  |
| `target_login` | `string` |  |
| `events_were` | `array` |  |
| `business` | `string` |  |
| `previous_visibility` | `string` |  |
| `org_id` | `integer` |  |
| `events` | `array` |  |
| `actor` | `string` | The actor who performed the action. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `data` | `object` |  |
| `content_type` | `string` |  |
| `limited_availability` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `enterprise` |
