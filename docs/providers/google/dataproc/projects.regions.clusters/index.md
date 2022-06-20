---
title: projects.regions.clusters
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
<tr><td><b>Name</b></td><td><code>projects.regions.clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.projects.regions.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListClustersRequest. |
| `clusters` | `array` | Output only. The clusters in the project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, projectId, region` | Gets the resource representation for a cluster in a project. |
| `list` | `SELECT` | `projectId, region` | Lists all regions/{region}/clusters in a project alphabetically. |
| `create` | `INSERT` | `projectId, region` | Creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| `delete` | `DELETE` | `clusterName, projectId, region` | Deletes a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). |
| `diagnose` | `EXEC` | `clusterName, projectId, region` | Gets cluster diagnostic information. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). After the operation completes, Operation.response contains DiagnoseClusterResults (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults). |
| `getIamPolicy` | `EXEC` | `clustersId, projectsId, regionsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `injectCredentials` | `EXEC` | `clustersId, projectsId, regionsId` | Inject encrypted credentials into all of the VMs in a cluster.The target cluster must be a personal auth cluster assigned to the user who is issuing the RPC. |
| `patch` | `EXEC` | `clusterName, projectId, region` | Updates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata). The cluster must be in a RUNNING state or an error is returned. |
| `repair` | `EXEC` | `clusterName, projectId, region` | Repairs a cluster. |
| `setIamPolicy` | `EXEC` | `clustersId, projectsId, regionsId` | Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors. |
| `start` | `EXEC` | `clusterName, projectId, region` | Starts a cluster in a project. |
| `stop` | `EXEC` | `clusterName, projectId, region` | Stops a cluster in a project. |
| `testIamPermissions` | `EXEC` | `clustersId, projectsId, regionsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
