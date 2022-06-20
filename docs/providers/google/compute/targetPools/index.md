---
title: targetPools
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
<tr><td><b>Name</b></td><td><code>targetPools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.targetPools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#targetPool for target pools. |
| `failoverRatio` | `number` | This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool (i.e., not as a backup pool to some other target pool). The value of the field must be in [0, 1]. If set, backupPool must also be set. They together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below this number, traffic arriving at the load-balanced IP will be directed to the backup pool. In case where failoverRatio is not set or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy. |
| `instances` | `array` | A list of resource URLs to the virtual machine instances serving this pool. They must live in zones contained in the same region as this pool. |
| `sessionAffinity` | `string` | Session affinity option, must be one of the following values: NONE: Connections from the same client IP may go to any instance in the pool. CLIENT_IP: Connections from the same client IP will go to the same instance in the pool while that instance remains healthy. CLIENT_IP_PROTO: Connections from the same client IP with the same IP protocol will go to the same instance in the pool while that instance remains healthy. |
| `region` | `string` | [Output Only] URL of the region where the target pool resides. |
| `healthChecks` | `array` | The URL of the HttpHealthCheck resource. A member instance in this pool is considered healthy if and only if the health checks pass. Only legacy HttpHealthChecks are supported. Only one health check may be specified. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `backupPool` | `string` | The server-defined URL for the resource. This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool, and its failoverRatio field is properly set to a value between [0, 1]. backupPool and failoverRatio together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below failoverRatio, traffic arriving at the load-balanced IP will be directed to the backup pool. In case where failoverRatio and backupPool are not set, or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, region, targetPool` | Returns the specified target pool. Gets a list of available target pools by making a list() request. |
| `list` | `SELECT` | `project, region` | Retrieves a list of target pools available to the specified project and region. |
| `insert` | `INSERT` | `project, region` | Creates a target pool in the specified project and region using the data included in the request. |
| `delete` | `DELETE` | `project, region, targetPool` | Deletes the specified target pool. |
| `addHealthCheck` | `EXEC` | `project, region, targetPool` | Adds health check URLs to a target pool. |
| `addInstance` | `EXEC` | `project, region, targetPool` | Adds an instance to a target pool. |
| `aggregatedList` | `EXEC` | `project` | Retrieves an aggregated list of target pools. |
| `getHealth` | `EXEC` | `project, region, targetPool` | Gets the most recent health check results for each IP for the instance that is referenced by the given target pool. |
| `removeHealthCheck` | `EXEC` | `project, region, targetPool` | Removes health check URL from a target pool. |
| `removeInstance` | `EXEC` | `project, region, targetPool` | Removes instance URL from a target pool. |
| `setBackup` | `EXEC` | `project, region, targetPool` | Changes a backup target pool's configurations. |