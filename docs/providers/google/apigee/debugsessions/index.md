---
title: debugsessions
hide_title: false
hide_table_of_contents: false
keywords:
  - debugsessions
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
<tr><td><b>Name</b></td><td><code>debugsessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.debugsessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A unique ID for this DebugSession. |
| `timeout` | `string` | Optional. The time in seconds after which this DebugSession should end. This value will override the value in query param, if both are provided. |
| `tracesize` | `integer` | Optional. The maximum number of bytes captured from the response payload. Min = 0, Max = 5120, Default = 5120. |
| `validity` | `integer` | Optional. The length of time, in seconds, that this debug session is valid, starting from when it's received in the control plane. Min = 1, Max = 15, Default = 10. |
| `count` | `integer` | Optional. The number of request to be traced. Min = 1, Max = 15, Default = 10. |
| `createTime` | `string` | Output only. The first transaction creation timestamp, recorded by UAP. |
| `filter` | `string` | Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_apis_revisions_debugsessions_get` | `SELECT` | `name` | Retrieves a debug session. |
| `organizations_environments_apis_revisions_debugsessions_list` | `SELECT` | `parent` | Lists debug sessions that are currently active in the given API Proxy revision. |
| `organizations_environments_apis_revisions_debugsessions_create` | `INSERT` | `parent` | Creates a debug session for a deployed API Proxy revision. |
