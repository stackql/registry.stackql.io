---
title: attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - attributes
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | API key of the attribute. |
| `value` | `string` | Value of the attribute. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apiproducts_attributes_get` | `SELECT` | `name` | Gets the value of an API product attribute. |
| `organizations_apiproducts_attributes_list` | `SELECT` | `parent` | Lists all API product attributes. |
| `organizations_developers_apps_attributes_get` | `SELECT` | `name` | Returns a developer app attribute. |
| `organizations_developers_apps_attributes_list` | `SELECT` | `parent` | Returns a list of all developer app attributes. |
| `organizations_developers_attributes_get` | `SELECT` | `name` | Returns the value of the specified developer attribute. |
| `organizations_developers_attributes_list` | `SELECT` | `parent` | Returns a list of all developer attributes. |
| `organizations_apiproducts_attributes_delete` | `DELETE` | `name` | Deletes an API product attribute. |
| `organizations_developers_apps_attributes_delete` | `DELETE` | `name` | Deletes a developer app attribute. |
| `organizations_developers_attributes_delete` | `DELETE` | `name` | Deletes a developer attribute. |
| `organizations_apiproducts_attributes_updateApiProductAttribute` | `EXEC` | `name` | Updates the value of an API product attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with entities also get cached for at least 180 seconds after entity is accessed during runtime. In this case, the `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| `organizations_developers_apps_attributes_updateDeveloperAppAttribute` | `EXEC` | `name` | Updates a developer app attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| `organizations_developers_attributes_updateDeveloperAttribute` | `EXEC` | `name` | Updates a developer attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
