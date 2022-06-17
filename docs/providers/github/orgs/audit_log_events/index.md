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
| `emoji` | `string` |  |
| `active` | `boolean` |  |
| `target_login` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `repository_public` | `boolean` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `openssh_public_key` | `string` |  |
| `deploy_key_fingerprint` | `string` |  |
| `previous_visibility` | `string` |  |
| `actor_location` | `object` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `repository` | `string` | The name of the repository. |
| `active_was` | `boolean` |  |
| `explanation` | `string` |  |
| `events` | `array` |  |
| `actor` | `string` | The actor who performed the action. |
| `business` | `string` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `org_id` | `integer` |  |
| `old_user` | `string` |  |
| `config` | `array` |  |
| `team` | `string` |  |
| `config_was` | `array` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `hook_id` | `integer` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `data` | `object` |  |
| `limited_availability` | `boolean` |  |
| `message` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `fingerprint` | `string` |  |
| `read_only` | `boolean` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `repo` | `string` | The name of the repository. |
| `content_type` | `string` |  |
| `org` | `string` |  |
| `events_were` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `org` |
