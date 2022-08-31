---
title: product_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - product_deployments
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>product_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.product_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `subscriptionId` | `string` | The product subscription identifier |
| `type` | `string` | Type of Resource. |
| `deployment` | `object` | Resource provider deployment information |
| `productId` | `string` | The product identifier |
| `location` | `string` | Location of the resource. |
| `lastSuccessfulDeployment` | `object` | Resource provider deployment information |
| `eTag` | `string` | entity tag |
| `provisioningState` | `string` | The provisioning state |
| `internalState` | `object` | Resource type internal state |
| `secretRotation` | `object` | Resource provider deployment information |
| `externalAccess` | `object` | Resource provider deployment information |
| `error` | `object` | Error response. |
| `status` | `string` | Status of an operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ProductDeployments_List` | `SELECT` | `subscriptionId` |
| `ProductDeployments_Get` | `EXEC` | `productId, subscriptionId` |