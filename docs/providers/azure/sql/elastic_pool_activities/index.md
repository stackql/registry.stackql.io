---
title: elastic_pool_activities
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pool_activities
  - sql
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
<tr><td><b>Name</b></td><td><code>elastic_pool_activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pool_activities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `requestedDtuGuarantee` | `integer` | The requested DTU guarantee. |
| `requestedDatabaseDtuGuarantee` | `integer` | The requested per database DTU guarantee. |
| `startTime` | `string` | The time the operation started (ISO8601 format). |
| `endTime` | `string` | The time the operation finished (ISO8601 format). |
| `errorSeverity` | `integer` | The error severity if available. |
| `requestedDtu` | `integer` | The requested DTU for the pool if available. |
| `state` | `string` | The current state of the operation. |
| `percentComplete` | `integer` | The percentage complete if available. |
| `requestedStorageLimitInMB` | `integer` | The requested storage limit in MB. |
| `requestedDatabaseDtuMax` | `integer` | The requested max DTU per database if available. |
| `errorCode` | `integer` | The error code if available. |
| `location` | `string` | The geo-location where the resource lives |
| `operation` | `string` | The operation name. |
| `requestedDatabaseDtuCap` | `integer` | The requested per database DTU cap. |
| `operationId` | `string` | The unique operation ID. |
| `requestedElasticPoolName` | `string` | The requested name for the elastic pool if available. |
| `errorMessage` | `string` | The error message if available. |
| `serverName` | `string` | The name of the server the elastic pool is in. |
| `requestedStorageLimitInGB` | `integer` | The requested storage limit for the pool in GB if available. |
| `requestedDatabaseDtuMin` | `integer` | The requested min DTU per database if available. |
| `elasticPoolName` | `string` | The name of the elastic pool. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ElasticPoolActivities_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` |
