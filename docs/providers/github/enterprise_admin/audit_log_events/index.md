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
<tr><td><b>Name</b></td><td><code>github.enterprise_admin.audit_log_events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.audit_log_events</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `emoji` | `string` |  |
| `org_id` | `integer` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `previous_visibility` | `string` |  |
| `old_user` | `string` |  |
| `content_type` | `string` |  |
| `actor_location` | `object` |  |
| `actor` | `string` | The actor who performed the action. |
| `business` | `string` |  |
| `events_were` | `array` |  |
| `openssh_public_key` | `string` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `org` | `string` |  |
| `read_only` | `boolean` |  |
| `repository_public` | `boolean` |  |
| `team` | `string` |  |
| `events` | `array` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `repo` | `string` | The name of the repository. |
| `deploy_key_fingerprint` | `string` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `config` | `array` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `blocked_user` | `string` | The username of the account being blocked. |
| `config_was` | `array` |  |
| `explanation` | `string` |  |
| `data` | `object` |  |
| `active_was` | `boolean` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `target_login` | `string` |  |
| `active` | `boolean` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `repository` | `string` | The name of the repository. |
| `message` | `string` |  |
| `hook_id` | `integer` |  |
| `fingerprint` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `limited_availability` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_audit_log` | `enterprise` | Gets the audit log for an enterprise. To use this endpoint, you must be an enterprise admin, and you must use an access token with the `admin:enterprise` scope. | SELECT |
