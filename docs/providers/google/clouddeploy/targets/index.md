---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
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
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Name of the `Target`. Format is projects/{project}/locations/{location}/targets/a-z{0,62}. |
| `description` | `string` | Optional. Description of the `Target`. Max length is 255 characters. |
| `targetId` | `string` | Output only. Resource id of the `Target`. |
| `gke` | `object` | Information specifying a GKE Cluster. |
| `updateTime` | `string` | Output only. Most recent time at which the `Target` was updated. |
| `anthosCluster` | `object` | Information specifying an Anthos Cluster. |
| `requireApproval` | `boolean` | Optional. Whether or not the `Target` requires approval. |
| `uid` | `string` | Output only. Unique identifier of the `Target`. |
| `createTime` | `string` | Output only. Time at which the `Target` was created. |
| `labels` | `object` | Optional. Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| `etag` | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `executionConfigs` | `array` | Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`. |
| `annotations` | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_targets_get` | `SELECT` | `name` | Gets details of a single Target. |
| `projects_locations_targets_list` | `SELECT` | `parent` | Lists Targets in a given project and location. |
| `projects_locations_targets_create` | `INSERT` | `parent` | Creates a new Target in a given project and location. |
| `projects_locations_targets_delete` | `DELETE` | `name` | Deletes a single Target. |
| `projects_locations_targets_patch` | `EXEC` | `name` | Updates the parameters of a single Target. |
