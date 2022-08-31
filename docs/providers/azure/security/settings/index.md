---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - security
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
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `kind` | `string` | the kind of the settings string |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Settings_List` | `SELECT` | `api-version, subscriptionId` | Settings about different configurations in Microsoft Defender for Cloud |
| `Settings_Get` | `EXEC` | `api-version, settingName, subscriptionId` | Settings of different configurations in Microsoft Defender for Cloud |
| `Settings_Update` | `EXEC` | `api-version, settingName, subscriptionId, data__kind` | updating settings about different configurations in Microsoft Defender for Cloud |