---
title: mute_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - mute_configs
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
<tr><td><b>Name</b></td><td><code>mute_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.mute_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | This field will be ignored if provided on config creation. Format "organizations/{organization}/muteConfigs/{mute_config}" "folders/{folder}/muteConfigs/{mute_config}" "projects/{project}/muteConfigs/{mute_config}" |
| `description` | `string` | A description of the mute config. |
| `createTime` | `string` | Output only. The time at which the mute config was created. This field is set by the server and will be ignored if provided on config creation. |
| `displayName` | `string` | The human readable name to be displayed for the mute config. |
| `filter` | `string` | Required. An expression that defines the filter to apply across create/update events of findings. While creating a filter string, be mindful of the scope in which the mute configuration is being created. E.g., If a filter contains project = X but is created under the project = Y scope, it might not match any findings. The following field and operator combinations are supported: * severity: `=`, `:` * category: `=`, `:` * resource.name: `=`, `:` * resource.project_name: `=`, `:` * resource.project_display_name: `=`, `:` * resource.folders.resource_folder: `=`, `:` * resource.parent_name: `=`, `:` * resource.parent_display_name: `=`, `:` * resource.type: `=`, `:` * finding_class: `=`, `:` * indicator.ip_addresses: `=`, `:` * indicator.domains: `=`, `:` |
| `mostRecentEditor` | `string` | Output only. Email address of the user who last edited the mute config. This field is set by the server and will be ignored if provided on config creation or update. |
| `updateTime` | `string` | Output only. The most recent time at which the mute config was updated. This field is set by the server and will be ignored if provided on config creation or update. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_muteConfigs_get` | `SELECT` | `name` | Gets a mute config. |
| `folders_muteConfigs_list` | `SELECT` | `parent` | Lists mute configs. |
| `organizations_muteConfigs_get` | `SELECT` | `name` | Gets a mute config. |
| `organizations_muteConfigs_list` | `SELECT` | `parent` | Lists mute configs. |
| `projects_muteConfigs_get` | `SELECT` | `name` | Gets a mute config. |
| `projects_muteConfigs_list` | `SELECT` | `parent` | Lists mute configs. |
| `folders_muteConfigs_create` | `INSERT` | `parent` | Creates a mute config. |
| `organizations_muteConfigs_create` | `INSERT` | `parent` | Creates a mute config. |
| `projects_muteConfigs_create` | `INSERT` | `parent` | Creates a mute config. |
| `folders_muteConfigs_delete` | `DELETE` | `name` | Deletes an existing mute config. |
| `organizations_muteConfigs_delete` | `DELETE` | `name` | Deletes an existing mute config. |
| `projects_muteConfigs_delete` | `DELETE` | `name` | Deletes an existing mute config. |
| `folders_muteConfigs_patch` | `EXEC` | `name` | Updates a mute config. |
| `organizations_muteConfigs_patch` | `EXEC` | `name` | Updates a mute config. |
| `projects_muteConfigs_patch` | `EXEC` | `name` | Updates a mute config. |