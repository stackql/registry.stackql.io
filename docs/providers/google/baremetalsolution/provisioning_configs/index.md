---
title: provisioning_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - provisioning_configs
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.provisioning_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the provisioning config. |
| `handoverServiceAccount` | `string` | A service account to enable customers to access instance credentials upon handover. |
| `cloudConsoleUri` | `string` | Output only. URI to Cloud Console UI view of this provisioning config. |
| `instances` | `array` | Instances to be created. |
| `networks` | `array` | Networks to be created. |
| `location` | `string` | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |
| `updateTime` | `string` | Output only. Last update timestamp. |
| `volumes` | `array` | Volumes to be created. |
| `ticketId` | `string` | A generated ticket id to track provisioning request. |
| `email` | `string` | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |
| `state` | `string` | Output only. State of ProvisioningConfig. |
| `statusMessage` | `string` | Optional status messages associated with the FAILED state. |
| `vpcScEnabled` | `boolean` | If true, VPC SC is enabled for the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_provisioningConfigs_get` | `SELECT` | `name` | Get ProvisioningConfig by name. |
| `projects_locations_provisioningConfigs_create` | `INSERT` | `parent` | Create new ProvisioningConfig. |
| `projects_locations_provisioningConfigs_patch` | `EXEC` | `name` | Update existing ProvisioningConfig. |
| `projects_locations_provisioningConfigs_submit` | `EXEC` | `parent` | Submit a provisiong configuration for a given project. |
