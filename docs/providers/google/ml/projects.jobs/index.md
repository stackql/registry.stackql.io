---
title: projects.jobs
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
<tr><td><b>Name</b></td><td><code>projects.jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.projects.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobs` | `array` | The list of jobs. |
| `nextPageToken` | `string` | Optional. Pass this token as the `page_token` field of the request for a subsequent call. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `list` | `SELECT` | `projectsId` | Lists the jobs in the project. If there are no jobs that match the request parameters, the list request returns an empty response body: {}. |
| `create` | `INSERT` | `projectsId` | Creates a training or a batch prediction job. |
| `cancel` | `EXEC` | `jobsId, projectsId` | Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`. |
| `getIamPolicy` | `EXEC` | `jobsId, projectsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `patch` | `EXEC` | `jobsId, projectsId` | Updates the specified Version resource. Currently the only update-able fields are `description`, `requestLoggingConfig`, `autoScaling.minNodes`, and `manualScaling.nodes`. |
| `setIamPolicy` | `EXEC` | `jobsId, projectsId` | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| `testIamPermissions` | `EXEC` | `jobsId, projectsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
