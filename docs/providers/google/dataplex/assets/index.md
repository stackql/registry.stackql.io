---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the asset, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}. |
| `description` | `string` | Optional. Description of the asset. |
| `securityStatus` | `object` | Security policy status of the asset. Data security policy, i.e., readers, writers & owners, should be specified in the lake/zone/asset IAM policy. |
| `state` | `string` | Output only. Current state of the asset. |
| `uid` | `string` | Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name. |
| `resourceStatus` | `object` | Status of the resource referenced by an asset. |
| `updateTime` | `string` | Output only. The time when the asset was last updated. |
| `discoverySpec` | `object` | Settings to manage the metadata discovery and publishing for an asset. |
| `displayName` | `string` | Optional. User friendly display name. |
| `resourceSpec` | `object` | Identifies the cloud resource that is referenced by this asset. |
| `labels` | `object` | Optional. User defined labels for the asset. |
| `discoveryStatus` | `object` | Status of discovery for an asset. |
| `createTime` | `string` | Output only. The time when the asset was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_assets_get` | `SELECT` | `name` | Retrieves an asset resource. |
| `projects_locations_lakes_zones_assets_list` | `SELECT` | `parent` | Lists asset resources in a zone. |
| `projects_locations_lakes_zones_assets_create` | `INSERT` | `parent` | Creates an asset resource. |
| `projects_locations_lakes_zones_assets_delete` | `DELETE` | `name` | Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy. |
| `projects_locations_lakes_zones_assets_patch` | `EXEC` | `name` | Updates an asset resource. |
