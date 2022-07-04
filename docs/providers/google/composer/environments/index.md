---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.composer.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. |
| `state` | `string` | The current state of the environment. |
| `updateTime` | `string` | Output only. The time at which this environment was last modified. |
| `uuid` | `string` | Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created. |
| `config` | `object` | Configuration information for an environment. |
| `createTime` | `string` | Output only. The time at which this environment was created. |
| `labels` | `object` | Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p{Ll}\p{Lo}{0,62} * Values must conform to regexp: [\p{Ll}\p{Lo}\p{N}_-]{0,63} * Both keys and values are additionally constrained to be &lt;= 128 bytes in size. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_environments_get` | `SELECT` | `name` | Get an existing environment. |
| `projects_locations_environments_list` | `SELECT` | `parent` | List environments. |
| `projects_locations_environments_create` | `INSERT` | `parent` | Create a new environment. |
| `projects_locations_environments_delete` | `DELETE` | `name` | Delete an environment. |
| `projects_locations_environments_patch` | `EXEC` | `name` | Update an environment. |