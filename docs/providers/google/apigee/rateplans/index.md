---
title: rateplans
hide_title: false
hide_table_of_contents: false
keywords:
  - rateplans
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
<tr><td><b>Name</b></td><td><code>rateplans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.rateplans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the rate plan. |
| `description` | `string` | Description of the rate plan. |
| `paymentFundingModel` | `string` | DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the `billingType` field inside `DeveloperMonetizationConfig` resource. Flag that specifies the billing account type, prepaid or postpaid. |
| `createdAt` | `string` | Output only. Time that the rate plan was created in milliseconds since epoch. |
| `displayName` | `string` | Display name of the rate plan. |
| `fixedFeeFrequency` | `integer` | Frequency at which the fixed fee is charged. |
| `billingPeriod` | `string` | Frequency at which the customer will be billed. |
| `apiproduct` | `string` | Name of the API product that the rate plan is associated with. |
| `consumptionPricingRates` | `array` | API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200. |
| `revenueShareType` | `string` | Method used to calculate the revenue that is shared with developers. |
| `endTime` | `string` | Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire. |
| `startTime` | `string` | Time when the rate plan becomes active in milliseconds since epoch. |
| `setupFee` | `object` | Represents an amount of money with its currency type. |
| `consumptionPricingType` | `string` | Pricing model used for consumption-based charges. |
| `fixedRecurringFee` | `object` | Represents an amount of money with its currency type. |
| `state` | `string` | Current state of the rate plan (draft or published). |
| `revenueShareRates` | `array` | Details of the revenue sharing model. |
| `currencyCode` | `string` | Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard. |
| `lastModifiedAt` | `string` | Output only. Time the rate plan was last modified in milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apiproducts_rateplans_get` | `SELECT` | `name` | Gets the details of a rate plan. |
| `organizations_apiproducts_rateplans_list` | `SELECT` | `parent` | Lists all the rate plans for an API product. |
| `organizations_apiproducts_rateplans_create` | `INSERT` | `parent` | Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer's perspective, they purchase API products not rate plans. |
| `organizations_apiproducts_rateplans_delete` | `DELETE` | `name` | Deletes a rate plan. |
| `organizations_apiproducts_rateplans_update` | `EXEC` | `name` | Updates an existing rate plan. |