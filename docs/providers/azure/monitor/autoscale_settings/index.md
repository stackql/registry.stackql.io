---
title: autoscale_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscale_settings
  - monitor
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autoscale_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.autoscale_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | the name of the autoscale setting. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `enabled` | `boolean` | the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'false'. |
| `targetResourceLocation` | `string` | the location of the resource that the autoscale setting should be added to. |
| `profiles` | `array` | the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified. |
| `targetResourceUri` | `string` | the resource identifier of the resource that the autoscale setting should be added to. |
| `notifications` | `array` | the collection of notifications. |
| `predictiveAutoscalePolicy` | `object` | The parameters for enabling predictive autoscale. |
| `location` | `string` | Resource location |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AutoscaleSettings_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the autoscale settings for a resource group |
| `AutoscaleSettings_ListBySubscription` | `SELECT` | `subscriptionId` | Lists the autoscale settings for a subscription |
| `AutoscaleSettings_CreateOrUpdate` | `INSERT` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Creates or updates an autoscale setting. |
| `AutoscaleSettings_Delete` | `DELETE` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Deletes and autoscale setting |
| `AutoscaleSettings_Get` | `EXEC` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Gets an autoscale setting |
| `AutoscaleSettings_Update` | `EXEC` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method. |
