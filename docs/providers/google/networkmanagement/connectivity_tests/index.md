---
title: connectivity_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - connectivity_tests
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
<tr><td><b>Name</b></td><td><code>connectivity_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkmanagement.connectivity_tests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Unique name of the resource using the form: `projects/{project_id}/locations/global/connectivityTests/{test_id}` |
| `description` | `string` | The user-supplied description of the Connectivity Test. Maximum of 512 characters. |
| `displayName` | `string` | Output only. The display name of a Connectivity Test. |
| `relatedProjects` | `array` | Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries. |
| `destination` | `object` | Source or destination of the Connectivity Test. |
| `protocol` | `string` | IP Protocol of the test. When not provided, "TCP" is assumed. |
| `source` | `object` | Source or destination of the Connectivity Test. |
| `updateTime` | `string` | Output only. The time the test's configuration was updated. |
| `createTime` | `string` | Output only. The time the test was created. |
| `labels` | `object` | Resource labels to represent user-provided metadata. |
| `reachabilityDetails` | `object` | Results of the configuration analysis from the last run of the test. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_connectivityTests_get` | `SELECT` | `name` | Gets the details of a specific Connectivity Test. |
| `projects_locations_global_connectivityTests_list` | `SELECT` | `parent` | Lists all Connectivity Tests owned by a project. |
| `projects_locations_global_connectivityTests_create` | `INSERT` | `parent` | Creates a new Connectivity Test. After you create a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. If the endpoint specifications in `ConnectivityTest` are invalid (for example, containing non-existent resources in the network, or you don't have read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`. If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of AMBIGUOUS. For more information, see the Connectivity Test documentation. |
| `projects_locations_global_connectivityTests_delete` | `DELETE` | `name` | Deletes a specific `ConnectivityTest`. |
| `projects_locations_global_connectivityTests_patch` | `EXEC` | `name` | Updates the configuration of an existing `ConnectivityTest`. After you update a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. The Reachability state in the test resource is updated with the new result. If the endpoint specifications in `ConnectivityTest` are invalid (for example, they contain non-existent resources in the network, or the user does not have read permissions to the network configurations of listed projects), then the reachability result returns a value of UNKNOWN. If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of `AMBIGUOUS`. See the documentation in `ConnectivityTest` for for more details. |
| `projects_locations_global_connectivityTests_rerun` | `EXEC` | `name` | Rerun an existing `ConnectivityTest`. After the user triggers the rerun, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. Even though the test configuration remains the same, the reachability result may change due to underlying network configuration changes. If the endpoint specifications in `ConnectivityTest` become invalid (for example, specified resources are deleted in the network, or you lost read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`. |
