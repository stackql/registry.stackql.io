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
| `percentComplete` | `integer` | The percentage complete if available. |
| `serverName` | `string` | The name of the server the elastic pool is in. |
| `errorSeverity` | `integer` | The error severity if available. |
| `requestedStorageLimitInMB` | `integer` | The requested storage limit in MB. |
| `requestedDatabaseDtuMax` | `integer` | The requested max DTU per database if available. |
| `errorMessage` | `string` | The error message if available. |
| `location` | `string` | The geo-location where the resource lives |
| `startTime` | `string` | The time the operation started (ISO8601 format). |
| `errorCode` | `integer` | The error code if available. |
| `requestedDatabaseDtuGuarantee` | `integer` | The requested per database DTU guarantee. |
| `elasticPoolName` | `string` | The name of the elastic pool. |
| `requestedDtuGuarantee` | `integer` | The requested DTU guarantee. |
| `requestedElasticPoolName` | `string` | The requested name for the elastic pool if available. |
| `requestedStorageLimitInGB` | `integer` | The requested storage limit for the pool in GB if available. |
| `requestedDtu` | `integer` | The requested DTU for the pool if available. |
| `state` | `string` | The current state of the operation. |
| `operationId` | `string` | The unique operation ID. |
| `operation` | `string` | The operation name. |
| `requestedDatabaseDtuMin` | `integer` | The requested min DTU per database if available. |
| `requestedDatabaseDtuCap` | `integer` | The requested per database DTU cap. |
| `endTime` | `string` | The time the operation finished (ISO8601 format). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ElasticPoolActivities_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` |
