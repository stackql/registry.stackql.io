---
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
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
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.recommendations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of recommendation. |
| `description` | `string` | Free-form human readable summary in English. The maximum length is 500 characters. |
| `stateInfo` | `object` | Information for state. Contains state and metadata. |
| `etag` | `string` | Fingerprint of the Recommendation. Provides optimistic locking when updating states. |
| `lastRefreshTime` | `string` | Last time this recommendation was refreshed by the system that created it in the first place. |
| `recommenderSubtype` | `string` | Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender. Examples: For recommender = "google.iam.policy.Recommender", recommender_subtype can be one of "REMOVE_ROLE"/"REPLACE_ROLE" |
| `content` | `object` | Contains what resources are changing and how they are changing. |
| `additionalImpact` | `array` | Optional set of additional impact that this recommendation may have when trying to optimize for the primary category. These may be positive or negative. |
| `xorGroupId` | `string` | Corresponds to a mutually exclusive group ID within a recommender. A non-empty ID indicates that the recommendation belongs to a mutually exclusive group. This means that only one recommendation within the group is suggested to be applied. |
| `associatedInsights` | `array` | Insights that led to this recommendation. |
| `primaryImpact` | `object` | Contains the impact a recommendation can have for a given category. |
| `priority` | `string` | Recommendation's priority. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_recommenders_recommendations_get` | `SELECT` | `name` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_list` | `SELECT` | `parent` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_get` | `SELECT` | `name` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_list` | `SELECT` | `parent` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_get` | `SELECT` | `name` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_list` | `SELECT` | `parent` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_get` | `SELECT` | `name` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_list` | `SELECT` | `parent` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_markClaimed` | `EXEC` | `name` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_markFailed` | `EXEC` | `name` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `name` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_markClaimed` | `EXEC` | `name` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_markFailed` | `EXEC` | `name` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `name` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_markClaimed` | `EXEC` | `name` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_markFailed` | `EXEC` | `name` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `name` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_markClaimed` | `EXEC` | `name` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_markFailed` | `EXEC` | `name` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `name` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
