---
title: worker_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - worker_pools
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
<tr><td><b>Name</b></td><td><code>worker_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.worker_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{worker_pool}`. The value of `{worker_pool}` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `{location}` is determined by the endpoint accessed. |
| `privatePoolV1Config` | `object` | Configuration for a V1 `PrivatePool`. |
| `state` | `string` | Output only. `WorkerPool` state. |
| `annotations` | `object` | User specified annotations. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `uid` | `string` | Output only. A unique identifier for the `WorkerPool`. |
| `createTime` | `string` | Output only. Time at which the request to create the `WorkerPool` was received. |
| `deleteTime` | `string` | Output only. Time at which the request to delete the `WorkerPool` was received. |
| `displayName` | `string` | A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters. |
| `updateTime` | `string` | Output only. Time at which the request to update the `WorkerPool` was received. |
| `etag` | `string` | Output only. Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workerPools_get` | `SELECT` | `name` | Returns details of a `WorkerPool`. |
| `projects_locations_workerPools_list` | `SELECT` | `parent` | Lists `WorkerPool`s. |
| `projects_locations_workerPools_create` | `INSERT` | `parent` | Creates a `WorkerPool`. |
| `projects_locations_workerPools_delete` | `DELETE` | `name` | Deletes a `WorkerPool`. |
| `projects_locations_workerPools_patch` | `EXEC` | `name` | Updates a `WorkerPool`. |
