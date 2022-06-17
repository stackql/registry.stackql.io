---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>github.search.users</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.search.users</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `suspended_at` | `string` |  |
| `html_url` | `string` |  |
| `public_repos` | `integer` |  |
| `received_events_url` | `string` |  |
| `node_id` | `string` |  |
| `repos_url` | `string` |  |
| `gravatar_id` | `string` |  |
| `gists_url` | `string` |  |
| `type` | `string` |  |
| `public_gists` | `integer` |  |
| `events_url` | `string` |  |
| `updated_at` | `string` |  |
| `starred_url` | `string` |  |
| `created_at` | `string` |  |
| `bio` | `string` |  |
| `avatar_url` | `string` |  |
| `email` | `string` |  |
| `location` | `string` |  |
| `text_matches` | `array` |  |
| `subscriptions_url` | `string` |  |
| `score` | `number` |  |
| `company` | `string` |  |
| `following` | `integer` |  |
| `blog` | `string` |  |
| `followers_url` | `string` |  |
| `hireable` | `boolean` |  |
| `url` | `string` |  |
| `login` | `string` |  |
| `following_url` | `string` |  |
| `site_admin` | `boolean` |  |
| `followers` | `integer` |  |
| `organizations_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `users` | `q` | Find users via various criteria. This method returns up to 100 results [per page](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination).<br /><br />When searching for users, you can get text match metadata for the issue **login**, **email**, and **name** fields when you pass the `text-match` media type. For more details about highlighting search results, see [Text match metadata](https://docs.github.com/rest/reference/search#text-match-metadata). For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/rest/reference/search#text-match-metadata).<br /><br />For example, if you're looking for a list of popular users, you might try this query:<br /><br />`q=tom+repos:%3E42+followers:%3E1000`<br /><br />This query searches for users with the name `tom`. The results are restricted to users with more than 42 repositories and over 1,000 followers. | SELECT |
