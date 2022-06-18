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
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `explanation` | `string` |  |
| `business` | `string` |  |
| `repository_public` | `boolean` |  |
| `content_type` | `string` |  |
| `target_login` | `string` |  |
| `events` | `array` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `limited_availability` | `boolean` |  |
| `message` | `string` |  |
| `org` | `string` |  |
| `previous_visibility` | `string` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `old_user` | `string` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `active_was` | `boolean` |  |
| `actor` | `string` | The actor who performed the action. |
| `repo` | `string` | The name of the repository. |
| `team` | `string` |  |
| `repository` | `string` | The name of the repository. |
| `data` | `object` |  |
| `read_only` | `boolean` |  |
| `config_was` | `array` |  |
| `actor_location` | `object` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `hook_id` | `integer` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `fingerprint` | `string` |  |
| `config` | `array` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `emoji` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `deploy_key_fingerprint` | `string` |  |
| `active` | `boolean` |  |
| `openssh_public_key` | `string` |  |
| `org_id` | `integer` |  |
| `events_were` | `array` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_audit_log` | `SELECT` | `org` |
