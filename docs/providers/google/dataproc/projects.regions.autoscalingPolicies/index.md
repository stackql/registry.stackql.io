---
title: projects.regions.autoscalingPolicies
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
<tr><td><b>Name</b></td><td><code>projects.regions.autoscalingPolicies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.projects.regions.autoscalingPolicies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | Output only. This token is included in the response if there are more results to fetch. |
| `policies` | `array` | Output only. Autoscaling policies list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `autoscalingPoliciesId, projectsId, regionsId` | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| `list` | `SELECT` | `projectsId, regionsId` | Lists autoscaling policies in the project. |
| `create` | `INSERT` | `projectsId, regionsId` | Creates new autoscaling policy. |
| `delete` | `DELETE` | `autoscalingPoliciesId, projectsId, regionsId` | Deletes a workflow template. It does not cancel in-progress workflows. |
| `getIamPolicy` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `setIamPolicy` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors. |
| `testIamPermissions` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
| `update` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
