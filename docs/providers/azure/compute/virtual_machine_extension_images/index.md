---
title: virtual_machine_extension_images
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extension_images
  - compute
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
<tr><td><b>Name</b></td><td><code>virtual_machine_extension_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_extension_images</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineExtensionImages_Get` | `EXEC` | `location, publisherName, subscriptionId, type, version` | Gets a virtual machine extension image. |
| `VirtualMachineExtensionImages_ListTypes` | `EXEC` | `location, publisherName, subscriptionId` | Gets a list of virtual machine extension image types. |
| `VirtualMachineExtensionImages_ListVersions` | `EXEC` | `location, publisherName, subscriptionId, type` | Gets a list of virtual machine extension image versions. |
