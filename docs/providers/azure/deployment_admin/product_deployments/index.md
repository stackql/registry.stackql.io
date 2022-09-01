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
| `externalAccess` | `object` | Resource provider deployment information |
| `productId` | `string` | The product identifier |
| `internalState` | `object` | Resource type internal state |
| `lastSuccessfulDeployment` | `object` | Resource provider deployment information |
| `status` | `string` | Status of an operation. |
| `subscriptionId` | `string` | The product subscription identifier |
| `type` | `string` | Type of Resource. |
| `location` | `string` | Location of the resource. |
| `deployment` | `object` | Resource provider deployment information |
| `provisioningState` | `string` | The provisioning state |
| `eTag` | `string` | entity tag |
| `secretRotation` | `object` | Resource provider deployment information |
| `error` | `object` | Error response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ProductDeployments_List` | `SELECT` | `subscriptionId` |
| `ProductDeployments_Get` | `EXEC` | `productId, subscriptionId` |
