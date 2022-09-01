---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - traffic_manager
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.traffic_manager.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `monitorConfig` | `object` | Class containing endpoint monitoring settings in a Traffic Manager profile. |
| `profileStatus` | `string` | The status of the Traffic Manager profile. |
| `allowedEndpointRecordTypes` | `array` | The list of allowed endpoint record types. |
| `endpoints` | `array` | The list of endpoints in the Traffic Manager profile. |
| `location` | `string` | The Azure Region where the resource lives |
| `dnsConfig` | `object` | Class containing DNS settings in a Traffic Manager profile. |
| `trafficRoutingMethod` | `string` | The traffic routing method of the Traffic Manager profile. |
| `maxReturn` | `integer` | Maximum number of endpoints to be returned for MultiValue routing type. |
| `tags` | `object` | Resource tags. |
| `trafficViewEnrollmentStatus` | `string` | Indicates whether Traffic View is 'Enabled' or 'Disabled' for the Traffic Manager profile. Null, indicates 'Disabled'. Enabling this feature will increase the cost of the Traffic Manage profile. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Profiles_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Traffic Manager profiles within a resource group. |
| `Profiles_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all Traffic Manager profiles within a subscription. |
| `Profiles_CreateOrUpdate` | `INSERT` | `profileName, resourceGroupName, subscriptionId` | Create or update a Traffic Manager profile. |
| `Profiles_Delete` | `DELETE` | `profileName, resourceGroupName, subscriptionId` | Deletes a Traffic Manager profile. |
| `Profiles_CheckTrafficManagerRelativeDnsNameAvailability` | `EXEC` |  | Checks the availability of a Traffic Manager Relative DNS name. |
| `Profiles_Get` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Gets a Traffic Manager profile. |
| `Profiles_Update` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Update a Traffic Manager profile. |
