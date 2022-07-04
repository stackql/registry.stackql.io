---
title: phrase_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - phrase_sets
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
<tr><td><b>Name</b></td><td><code>phrase_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.speech.phrase_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the phrase set. |
| `phrases` | `array` | A list of word and phrases. |
| `boost` | `number` | Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 (exclusive) and 20. We recommend using a binary search approach to finding the optimal value for your use case. Speech recognition will skip PhraseSets with a boost value of 0. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_phraseSets_get` | `SELECT` | `name` | Get a phrase set. |
| `projects_locations_phraseSets_list` | `SELECT` | `parent` | List phrase sets. |
| `projects_locations_phraseSets_create` | `INSERT` | `parent` | Create a set of phrase hints. Each item in the set can be a single word or a multi-word phrase. The items in the PhraseSet are favored by the recognition model when you send a call that includes the PhraseSet. |
| `projects_locations_phraseSets_delete` | `DELETE` | `name` | Delete a phrase set. |
| `projects_locations_phraseSets_patch` | `EXEC` | `name` | Update a phrase set. |
