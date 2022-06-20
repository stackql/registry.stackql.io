---
title: healthChecks
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
<tr><td><b>Name</b></td><td><code>healthChecks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.healthChecks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `type` | `string` | Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field. |
| `timeoutSec` | `integer` | How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. |
| `http2HealthCheck` | `object` |  |
| `unhealthyThreshold` | `integer` | A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. |
| `kind` | `string` | Type of the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in 3339 text format. |
| `grpcHealthCheck` | `object` |  |
| `httpsHealthCheck` | `object` |  |
| `tcpHealthCheck` | `object` |  |
| `checkIntervalSec` | `integer` | How often (in seconds) to send a health check. The default value is 5 seconds. |
| `httpHealthCheck` | `object` |  |
| `sslHealthCheck` | `object` |  |
| `healthyThreshold` | `integer` | A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. |
| `region` | `string` | [Output Only] Region where the health check resides. Not applicable to global health checks. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `logConfig` | `object` | Configuration of logging on a health check. If logging is enabled, logs will be exported to Stackdriver. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `healthCheck, project` | Returns the specified HealthCheck resource. Gets a list of available health checks by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of HealthCheck resources available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a HealthCheck resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `healthCheck, project` | Deletes the specified HealthCheck resource. |
| `aggregatedList` | `EXEC` | `project` | Retrieves the list of all HealthCheck resources, regional and global, available to the specified project. |
| `patch` | `EXEC` | `healthCheck, project` | Updates a HealthCheck resource in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `update` | `EXEC` | `healthCheck, project` | Updates a HealthCheck resource in the specified project using the data included in the request. |
