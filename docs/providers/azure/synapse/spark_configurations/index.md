---
title: spark_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - spark_configurations
  - synapse
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
<tr><td><b>Name</b></td><td><code>spark_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.spark_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Description about the SparkConfiguration. |
| `configs` | `object` | SparkConfiguration configs. |
| `created` | `string` | The timestamp of resource creation. |
| `createdBy` | `string` | The identity that created the resource. |
| `notes` | `string` | additional Notes. |
| `annotations` | `array` | Annotations for SparkConfiguration. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SparkConfigurations_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
