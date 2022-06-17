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
<tr><td><b>Name</b></td><td><code>github.orgs.audit_log_events</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.audit_log_events</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `config_was` | `array` |  |
| `message` | `string` |  |
| `repository_public` | `boolean` |  |
| `org` | `string` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `deploy_key_fingerprint` | `string` |  |
| `org_id` | `integer` |  |
| `target_login` | `string` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `active_was` | `boolean` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `config` | `array` |  |
| `fingerprint` | `string` |  |
| `team` | `string` |  |
| `explanation` | `string` |  |
| `previous_visibility` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `actor_location` | `object` |  |
| `repo` | `string` | The name of the repository. |
| `business` | `string` |  |
| `read_only` | `boolean` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `repository` | `string` | The name of the repository. |
| `data` | `object` |  |
| `limited_availability` | `boolean` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `openssh_public_key` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `events_were` | `array` |  |
| `hook_id` | `integer` |  |
| `content_type` | `string` |  |
| `emoji` | `string` |  |
| `actor` | `string` | The actor who performed the action. |
| `old_user` | `string` |  |
| `active` | `boolean` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `events` | `array` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_audit_log` | `org` | Gets the audit log for an organization. For more information, see "[Reviewing the audit log for your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization)."<br /><br />This endpoint is available for organizations on GitHub Enterprise Cloud. To use this endpoint, you must be an organization owner, and you must use an access token with the `admin:org` scope. GitHub Apps must have the `organization_administration` read permission to use this endpoint. | SELECT |
