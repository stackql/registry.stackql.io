---
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.insights</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the insight. |
| `description` | `string` | Free-form human readable summary in English. The maximum length is 500 characters. |
| `content` | `object` | A struct of custom fields to explain the insight. Example: "grantedPermissionsCount": "1000" |
| `associatedRecommendations` | `array` | Recommendations derived from this insight. |
| `severity` | `string` | Insight's severity. |
| `category` | `string` | Category being targeted by the insight. |
| `lastRefreshTime` | `string` | Timestamp of the latest data used to generate the insight. |
| `targetResources` | `array` | Fully qualified resource names that this insight is targeting. |
| `insightSubtype` | `string` | Insight subtype. Insight content schema will be stable for a given subtype. |
| `observationPeriod` | `string` | Observation period that led to the insight. The source data used to generate the insight ends at last_refresh_time and begins at (last_refresh_time - observation_period). |
| `stateInfo` | `object` | Information related to insight state. |
| `etag` | `string` | Fingerprint of the Insight. Provides optimistic locking when updating states. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_insightTypes_insights_get` | `SELECT` | `name` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `billingAccounts_locations_insightTypes_insights_list` | `SELECT` | `parent` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `folders_locations_insightTypes_insights_get` | `SELECT` | `name` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `folders_locations_insightTypes_insights_list` | `SELECT` | `parent` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `organizations_locations_insightTypes_insights_get` | `SELECT` | `name` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `organizations_locations_insightTypes_insights_list` | `SELECT` | `parent` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `projects_locations_insightTypes_insights_get` | `SELECT` | `name` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `projects_locations_insightTypes_insights_list` | `SELECT` | `parent` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `billingAccounts_locations_insightTypes_insights_markAccepted` | `EXEC` | `name` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| `folders_locations_insightTypes_insights_markAccepted` | `EXEC` | `name` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| `organizations_locations_insightTypes_insights_markAccepted` | `EXEC` | `name` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| `projects_locations_insightTypes_insights_markAccepted` | `EXEC` | `name` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
