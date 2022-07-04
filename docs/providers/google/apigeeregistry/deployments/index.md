---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. |
| `description` | `string` | A detailed description. |
| `createTime` | `string` | Output only. Creation timestamp; when the deployment resource was created. |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed. |
| `apiSpecRevision` | `string` | The full resource name (including revision id) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: apis/{api}/deployments/{deployment} |
| `displayName` | `string` | Human-meaningful name. |
| `revisionUpdateTime` | `string` | Output only. Last update timestamp: when the represented revision was last modified. |
| `endpointUri` | `string` | The address where the deployment is serving. Changes to this value will update the revision. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `intendedAudience` | `string` | Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision. |
| `revisionCreateTime` | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
| `externalChannelUri` | `string` | The address of the external channel of the API (e.g. the Developer Portal). Changes to this value will not affect the revision. |
| `accessGuidance` | `string` | Text briefly describing how to access the endpoint. Changes to this value will not affect the revision. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_deployments_get` | `SELECT` | `name` | GetApiDeployment returns a specified deployment. |
| `projects_locations_apis_deployments_list` | `SELECT` | `parent` | ListApiDeployments returns matching deployments. |
| `projects_locations_apis_deployments_create` | `INSERT` | `parent` | CreateApiDeployment creates a specified deployment. |
| `projects_locations_apis_deployments_delete` | `DELETE` | `name` | DeleteApiDeployment removes a specified deployment, all revisions, and all child resources (e.g. artifacts). |
| `projects_locations_apis_deployments_patch` | `EXEC` | `name` | UpdateApiDeployment can be used to modify a specified deployment. |
| `projects_locations_apis_deployments_rollback` | `EXEC` | `name` | RollbackApiDeployment sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| `projects_locations_apis_deployments_tagRevision` | `EXEC` | `name` | TagApiDeploymentRevision adds a tag to a specified revision of a deployment. |