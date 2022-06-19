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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `limited_availability` | `boolean` |  |
| `business` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `emoji` | `string` |  |
| `org_id` | `integer` |  |
| `repository` | `string` | The name of the repository. |
| `hook_id` | `integer` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `actor` | `string` | The actor who performed the action. |
| `previous_visibility` | `string` |  |
| `data` | `object` |  |
| `openssh_public_key` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `fingerprint` | `string` |  |
| `team` | `string` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `deploy_key_fingerprint` | `string` |  |
| `content_type` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `config` | `array` |  |
| `active_was` | `boolean` |  |
| `target_login` | `string` |  |
| `message` | `string` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `org` | `string` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `explanation` | `string` |  |
| `repository_public` | `boolean` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `actor_location` | `object` |  |
| `events` | `array` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `events_were` | `array` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `active` | `boolean` |  |
| `read_only` | `boolean` |  |
| `old_user` | `string` |  |
| `config_was` | `array` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `enterprise` |
