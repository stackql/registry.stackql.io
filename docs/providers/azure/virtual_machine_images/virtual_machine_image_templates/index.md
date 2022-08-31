---
title: virtual_machine_image_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates
  - virtual_machine_images
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
<tr><td><b>Name</b></td><td><code>virtual_machine_image_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.virtual_machine_images.virtual_machine_image_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `stagingResourceGroup` | `string` | The staging resource group id in the same subscription as the image template that will be used to build the image. If this field is empty, a resource group with a random name will be created. If the resource group specified in this field doesn't exist, it will be created with the same name. If the resource group specified exists, it must be empty and in the same region as the image template. The resource group created will be deleted during template deletion if this field is empty or the resource group specified doesn't exist, but if the resource group specified exists the resources created in the resource group will be deleted during template deletion and the resource group itself will remain. |
| `provisioningError` | `object` | Describes the error happened when create or update an image template |
| `lastRunStatus` | `object` | Describes the latest status of running an image template |
| `validate` | `object` | Configuration options and list of validations to be performed on the resulting image. |
| `distribute` | `array` | The distribution targets where the image output needs to go to. |
| `customize` | `array` | Specifies the properties used to describe the customization steps of the image, like Image source etc |
| `location` | `string` | The geo-location where the resource lives |
| `source` | `object` | Describes a virtual machine image source for building, customizing and distributing |
| `vmProfile` | `object` | Describes the virtual machines used to build and validate images |
| `buildTimeoutInMinutes` | `integer` | Maximum duration to wait while building the image template (includes all customizations, validations, and distributions). Omit or specify 0 to use the default (4 hours). |
| `provisioningState` | `string` | Provisioning state of the resource |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the image template. |
| `exactStagingResourceGroup` | `string` | The staging resource group id in the same subscription as the image template that will be used to build the image. This read-only field differs from 'stagingResourceGroup' only if the value specified in the 'stagingResourceGroup' field is empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineImageTemplates_List` | `SELECT` | `subscriptionId` | Gets information about the VM image templates associated with the subscription. |
| `VirtualMachineImageTemplates_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about the VM image templates associated with the specified resource group. |
| `VirtualMachineImageTemplates_CreateOrUpdate` | `INSERT` | `imageTemplateName, resourceGroupName, subscriptionId, data__identity` | Create or update a virtual machine image template |
| `VirtualMachineImageTemplates_Delete` | `DELETE` | `imageTemplateName, resourceGroupName, subscriptionId` | Delete a virtual machine image template |
| `VirtualMachineImageTemplates_Cancel` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Cancel the long running image build based on the image template |
| `VirtualMachineImageTemplates_Get` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Get information about a virtual machine image template |
| `VirtualMachineImageTemplates_GetRunOutput` | `EXEC` | `imageTemplateName, resourceGroupName, runOutputName, subscriptionId` | Get the specified run output for the specified image template resource |
| `VirtualMachineImageTemplates_ListRunOutputs` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | List all run outputs for the specified Image Template resource |
| `VirtualMachineImageTemplates_Run` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Create artifacts from a existing image template |
| `VirtualMachineImageTemplates_Update` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` | Update the tags for this Virtual Machine Image Template |
