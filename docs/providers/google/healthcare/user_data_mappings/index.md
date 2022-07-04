---
title: user_data_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_data_mappings
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
<tr><td><b>Name</b></td><td><code>user_data_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.user_data_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`. |
| `dataId` | `string` | Required. A unique identifier for the mapped resource. |
| `resourceAttributes` | `array` | Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `archiveTime` | `string` | Output only. Indicates the time when this mapping was archived. |
| `archived` | `boolean` | Output only. Indicates whether this mapping is archived. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_consentStores_userDataMappings_get` | `SELECT` | `name` | Gets the specified User data mapping. |
| `projects_locations_datasets_consentStores_userDataMappings_list` | `SELECT` | `parent` | Lists the User data mappings in the specified consent store. |
| `projects_locations_datasets_consentStores_userDataMappings_create` | `INSERT` | `parent` | Creates a new User data mapping in the parent consent store. |
| `projects_locations_datasets_consentStores_userDataMappings_delete` | `DELETE` | `name` | Deletes the specified User data mapping. |
| `projects_locations_datasets_consentStores_userDataMappings_archive` | `EXEC` | `name` | Archives the specified User data mapping. |
| `projects_locations_datasets_consentStores_userDataMappings_patch` | `EXEC` | `name` | Updates the specified User data mapping. |