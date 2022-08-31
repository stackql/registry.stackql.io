---
title: baselines
hide_title: false
hide_table_of_contents: false
keywords:
  - baselines
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
<tr><td><b>Name</b></td><td><code>baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.baselines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The metric baseline Id. |
| `name` | `string` | The name of the metric for which the baselines were retrieved. |
| `namespace` | `string` | The namespace of the metrics been queried. |
| `timespan` | `string` | The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned back from what was originally requested. |
| `type` | `string` | The resource type of the metric baseline resource. |
| `baselines` | `array` | The baseline for each time series that was queried. |
| `interval` | `string` | The interval (window size) for which the metric data was returned in.  This may be adjusted in the future and returned back from what was originally requested.  This is not present if a metadata request was made. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Baselines_List` | `SELECT` | `interval, metricName, metricNamespace, resourceUri, timespan` |
