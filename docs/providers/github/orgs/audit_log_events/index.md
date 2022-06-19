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
<tr><td><b>Id</b></td><td><code>github.orgs.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `hook_id` | `integer` |  |
| `emoji` | `string` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `fingerprint` | `string` |  |
| `config_was` | `array` |  |
| `business` | `string` |  |
| `read_only` | `boolean` |  |
| `active` | `boolean` |  |
| `repository` | `string` | The name of the repository. |
| `blocked_user` | `string` | The username of the account being blocked. |
| `data` | `object` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `message` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `org` | `string` |  |
| `actor_location` | `object` |  |
| `repository_public` | `boolean` |  |
| `config` | `array` |  |
| `content_type` | `string` |  |
| `events_were` | `array` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `org_id` | `integer` |  |
| `deploy_key_fingerprint` | `string` |  |
| `old_user` | `string` |  |
| `previous_visibility` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `openssh_public_key` | `string` |  |
| `limited_availability` | `boolean` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `actor` | `string` | The actor who performed the action. |
| `events` | `array` |  |
| `team` | `string` |  |
| `target_login` | `string` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `active_was` | `boolean` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `explanation` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `org` |
