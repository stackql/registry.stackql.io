---
title: public_maintenance_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - public_maintenance_configurations
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
<tr><td><b>Name</b></td><td><code>public_maintenance_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.public_maintenance_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `visibility` | `string` | Gets or sets the visibility of the configuration. The default value is 'Custom' |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `maintenanceScope` | `string` | Gets or sets maintenanceScope of the configuration |
| `maintenanceWindow` | `object` | Definition of a MaintenanceWindow |
| `tags` | `object` | Gets or sets tags of the resource |
| `location` | `string` | Gets or sets location of the resource |
| `namespace` | `string` | Gets or sets namespace of the resource |
| `extensionProperties` | `object` | Gets or sets extensionProperties of the maintenanceConfiguration |
| `installPatches` | `object` | Input configuration for a patch run |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PublicMaintenanceConfigurations_List` | `SELECT` | `subscriptionId` |
| `PublicMaintenanceConfigurations_Get` | `EXEC` | `resourceName, subscriptionId` |
