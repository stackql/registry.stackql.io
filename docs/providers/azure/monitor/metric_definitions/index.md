---
title: metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_definitions
  - monitor
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
<tr><td><b>Name</b></td><td><code>metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | the resource identifier of the metric definition. |
| `name` | `object` | The localizable string class. |
| `supportedAggregationTypes` | `array` | the collection of what aggregation types are supported. |
| `dimensions` | `array` | the name and the display name of the dimension, i.e. it is a localizable string. |
| `metricClass` | `string` | The class of the metric. |
| `unit` | `string` | The unit of the metric. |
| `namespace` | `string` | the namespace the metric belongs to. |
| `resourceId` | `string` | the resource identifier of the resource that emitted the metric. |
| `displayDescription` | `string` | Detailed description of this metric. |
| `metricAvailabilities` | `array` | the collection of what aggregation intervals are available to be queried. |
| `category` | `string` | Custom category name for this metric. |
| `isDimensionRequired` | `boolean` | Flag to indicate whether the dimension is required. |
| `primaryAggregationType` | `string` | the aggregation type of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MetricDefinitions_List` | `SELECT` | `metricNamespace, resourceUri` |
