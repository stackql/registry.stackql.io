---
title: configurations_for_resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations_for_resource_group
  - maintenance
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
<tr><td><b>Name</b></td><td><code>configurations_for_resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.configurations_for_resource_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `extensionProperties` | `object` | Gets or sets extensionProperties of the maintenanceConfiguration |
| `namespace` | `string` | Gets or sets namespace of the resource |
| `location` | `string` | Gets or sets location of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `installPatches` | `object` | Input configuration for a patch run |
| `maintenanceWindow` | `object` | Definition of a MaintenanceWindow |
| `maintenanceScope` | `string` | Gets or sets maintenanceScope of the configuration |
| `tags` | `object` | Gets or sets tags of the resource |
| `visibility` | `string` | Gets or sets the visibility of the configuration. The default value is 'Custom' |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MaintenanceConfigurationsForResourceGroup_List` | `SELECT` | `resourceGroupName, subscriptionId` |
