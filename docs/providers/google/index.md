---
title: google
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
A description of the provider.  
    

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL google v0.1.2;
```

## Authentication
```javascript
{
    "google": {
        /**
            * Type of authentication to use, suported values include: service_account, api_key, basic
            * @type String
            */
        "type": string, 
        /**
            * path to service account key file.
            * @type String
            */
        "credentialsfilepath": string, 
        /**
            * Environment variable name containing the api key or credentials.
            * @type String
            */
        "credentialsenvvar": string, 
        /**
            * Value prepended to the request header, e.g. "Bearer "
            * @type String
            */
        "valuePrefix": string, 
    }
}
```
### Example
```bash
AUTH='{ "google": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}
stackql shell --auth="${AUTH}"
```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/google/abusiveexperiencereport/">abusiveexperiencereport</a><br />
<a href="/providers/google/acceleratedmobilepageurl/">acceleratedmobilepageurl</a><br />
<a href="/providers/google/accessapproval/">accessapproval</a><br />
<a href="/providers/google/accesscontextmanager/">accesscontextmanager</a><br />
<a href="/providers/google/adexchangebuyer/">adexchangebuyer</a><br />
<a href="/providers/google/adexchangebuyer2/">adexchangebuyer2</a><br />
<a href="/providers/google/adexperiencereport/">adexperiencereport</a><br />
<a href="/providers/google/admin/">admin</a><br />
<a href="/providers/google/admob/">admob</a><br />
<a href="/providers/google/adsense/">adsense</a><br />
<a href="/providers/google/adsensehost/">adsensehost</a><br />
<a href="/providers/google/alertcenter/">alertcenter</a><br />
<a href="/providers/google/analytics/">analytics</a><br />
<a href="/providers/google/analyticsreporting/">analyticsreporting</a><br />
<a href="/providers/google/androiddeviceprovisioning/">androiddeviceprovisioning</a><br />
<a href="/providers/google/androidenterprise/">androidenterprise</a><br />
<a href="/providers/google/androidmanagement/">androidmanagement</a><br />
<a href="/providers/google/androidpublisher/">androidpublisher</a><br />
<a href="/providers/google/apigee/">apigee</a><br />
<a href="/providers/google/appengine/">appengine</a><br />
<a href="/providers/google/appsactivity/">appsactivity</a><br />
<a href="/providers/google/artifactregistry/">artifactregistry</a><br />
<a href="/providers/google/bigquery/">bigquery</a><br />
<a href="/providers/google/bigqueryconnection/">bigqueryconnection</a><br />
<a href="/providers/google/bigquerydatatransfer/">bigquerydatatransfer</a><br />
<a href="/providers/google/bigqueryreservation/">bigqueryreservation</a><br />
<a href="/providers/google/bigtableadmin/">bigtableadmin</a><br />
<a href="/providers/google/billingbudgets/">billingbudgets</a><br />
<a href="/providers/google/binaryauthorization/">binaryauthorization</a><br />
<a href="/providers/google/blogger/">blogger</a><br />
<a href="/providers/google/books/">books</a><br />
<a href="/providers/google/calendar/">calendar</a><br />
<a href="/providers/google/chat/">chat</a><br />
<a href="/providers/google/chromeuxreport/">chromeuxreport</a><br />
<a href="/providers/google/civicinfo/">civicinfo</a><br />
<a href="/providers/google/classroom/">classroom</a><br />
<a href="/providers/google/cloudasset/">cloudasset</a><br />
<a href="/providers/google/cloudbilling/">cloudbilling</a><br />
<a href="/providers/google/cloudbuild/">cloudbuild</a><br />
<a href="/providers/google/clouddebugger/">clouddebugger</a><br />
<a href="/providers/google/clouderrorreporting/">clouderrorreporting</a><br />
<a href="/providers/google/cloudfunctions/">cloudfunctions</a><br />
<a href="/providers/google/cloudidentity/">cloudidentity</a><br />
<a href="/providers/google/cloudiot/">cloudiot</a><br />
<a href="/providers/google/cloudkms/">cloudkms</a><br />
<a href="/providers/google/cloudprofiler/">cloudprofiler</a><br />
<a href="/providers/google/cloudresourcemanager/">cloudresourcemanager</a><br />
<a href="/providers/google/cloudscheduler/">cloudscheduler</a><br />
<a href="/providers/google/cloudsearch/">cloudsearch</a><br />
<a href="/providers/google/cloudshell/">cloudshell</a><br />
<a href="/providers/google/cloudtasks/">cloudtasks</a><br />
<a href="/providers/google/cloudtrace/">cloudtrace</a><br />
<a href="/providers/google/composer/">composer</a><br />
<a href="/providers/google/compute/">compute</a><br />
<a href="/providers/google/container/">container</a><br />
<a href="/providers/google/containeranalysis/">containeranalysis</a><br />
<a href="/providers/google/content/">content</a><br />
<a href="/providers/google/customsearch/">customsearch</a><br />
<a href="/providers/google/datacatalog/">datacatalog</a><br />
<a href="/providers/google/dataflow/">dataflow</a><br />
<a href="/providers/google/datafusion/">datafusion</a><br />
<a href="/providers/google/dataproc/">dataproc</a><br />
<a href="/providers/google/datastore/">datastore</a><br />
<a href="/providers/google/deploymentmanager/">deploymentmanager</a><br />
<a href="/providers/google/dfareporting/">dfareporting</a><br />
<a href="/providers/google/dialogflow/">dialogflow</a><br />
<a href="/providers/google/digitalassetlinks/">digitalassetlinks</a><br />
<a href="/providers/google/discovery/">discovery</a><br />
<a href="/providers/google/displayvideo/">displayvideo</a><br />
<a href="/providers/google/dlp/">dlp</a><br />
<a href="/providers/google/dns/">dns</a><br />
<a href="/providers/google/docs/">docs</a><br />
<a href="/providers/google/documentai/">documentai</a><br />
<a href="/providers/google/domainsrdap/">domainsrdap</a><br />
<a href="/providers/google/doubleclickbidmanager/">doubleclickbidmanager</a><br />
<a href="/providers/google/doubleclicksearch/">doubleclicksearch</a><br />
<a href="/providers/google/drive/">drive</a><br />
<a href="/providers/google/driveactivity/">driveactivity</a><br />
<a href="/providers/google/factchecktools/">factchecktools</a><br />
<a href="/providers/google/fcm/">fcm</a><br />
<a href="/providers/google/file/">file</a><br />
<a href="/providers/google/firebase/">firebase</a><br />
<a href="/providers/google/firebasedynamiclinks/">firebasedynamiclinks</a><br />
<a href="/providers/google/firebasehosting/">firebasehosting</a><br />
<a href="/providers/google/firebaseml/">firebaseml</a><br />
<a href="/providers/google/firebaserules/">firebaserules</a><br />
<a href="/providers/google/firestore/">firestore</a><br />
<a href="/providers/google/games/">games</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/google/gamesConfiguration/">gamesConfiguration</a><br />
<a href="/providers/google/gamesManagement/">gamesManagement</a><br />
<a href="/providers/google/gameservices/">gameservices</a><br />
<a href="/providers/google/genomics/">genomics</a><br />
<a href="/providers/google/gmail/">gmail</a><br />
<a href="/providers/google/gmailpostmastertools/">gmailpostmastertools</a><br />
<a href="/providers/google/groupssettings/">groupssettings</a><br />
<a href="/providers/google/healthcare/">healthcare</a><br />
<a href="/providers/google/homegraph/">homegraph</a><br />
<a href="/providers/google/iam/">iam</a><br />
<a href="/providers/google/iamcredentials/">iamcredentials</a><br />
<a href="/providers/google/iap/">iap</a><br />
<a href="/providers/google/identitytoolkit/">identitytoolkit</a><br />
<a href="/providers/google/indexing/">indexing</a><br />
<a href="/providers/google/jobs/">jobs</a><br />
<a href="/providers/google/kgsearch/">kgsearch</a><br />
<a href="/providers/google/language/">language</a><br />
<a href="/providers/google/libraryagent/">libraryagent</a><br />
<a href="/providers/google/licensing/">licensing</a><br />
<a href="/providers/google/lifesciences/">lifesciences</a><br />
<a href="/providers/google/logging/">logging</a><br />
<a href="/providers/google/managedidentities/">managedidentities</a><br />
<a href="/providers/google/manufacturers/">manufacturers</a><br />
<a href="/providers/google/memcache/">memcache</a><br />
<a href="/providers/google/ml/">ml</a><br />
<a href="/providers/google/monitoring/">monitoring</a><br />
<a href="/providers/google/networkmanagement/">networkmanagement</a><br />
<a href="/providers/google/oauth2/">oauth2</a><br />
<a href="/providers/google/osconfig/">osconfig</a><br />
<a href="/providers/google/oslogin/">oslogin</a><br />
<a href="/providers/google/pagespeedonline/">pagespeedonline</a><br />
<a href="/providers/google/people/">people</a><br />
<a href="/providers/google/playablelocations/">playablelocations</a><br />
<a href="/providers/google/playcustomapp/">playcustomapp</a><br />
<a href="/providers/google/plus/">plus</a><br />
<a href="/providers/google/policytroubleshooter/">policytroubleshooter</a><br />
<a href="/providers/google/poly/">poly</a><br />
<a href="/providers/google/prod_tt_sasportal/">prod_tt_sasportal</a><br />
<a href="/providers/google/pubsub/">pubsub</a><br />
<a href="/providers/google/pubsublite/">pubsublite</a><br />
<a href="/providers/google/realtimebidding/">realtimebidding</a><br />
<a href="/providers/google/recommendationengine/">recommendationengine</a><br />
<a href="/providers/google/recommender/">recommender</a><br />
<a href="/providers/google/redis/">redis</a><br />
<a href="/providers/google/remotebuildexecution/">remotebuildexecution</a><br />
<a href="/providers/google/reseller/">reseller</a><br />
<a href="/providers/google/run/">run</a><br />
<a href="/providers/google/runtimeconfig/">runtimeconfig</a><br />
<a href="/providers/google/safebrowsing/">safebrowsing</a><br />
<a href="/providers/google/sasportal/">sasportal</a><br />
<a href="/providers/google/script/">script</a><br />
<a href="/providers/google/searchconsole/">searchconsole</a><br />
<a href="/providers/google/secretmanager/">secretmanager</a><br />
<a href="/providers/google/securitycenter/">securitycenter</a><br />
<a href="/providers/google/serviceconsumermanagement/">serviceconsumermanagement</a><br />
<a href="/providers/google/servicecontrol/">servicecontrol</a><br />
<a href="/providers/google/servicedirectory/">servicedirectory</a><br />
<a href="/providers/google/servicemanagement/">servicemanagement</a><br />
<a href="/providers/google/servicenetworking/">servicenetworking</a><br />
<a href="/providers/google/serviceusage/">serviceusage</a><br />
<a href="/providers/google/sheets/">sheets</a><br />
<a href="/providers/google/siteVerification/">siteVerification</a><br />
<a href="/providers/google/slides/">slides</a><br />
<a href="/providers/google/sourcerepo/">sourcerepo</a><br />
<a href="/providers/google/spanner/">spanner</a><br />
<a href="/providers/google/speech/">speech</a><br />
<a href="/providers/google/sql/">sql</a><br />
<a href="/providers/google/storage/">storage</a><br />
<a href="/providers/google/storagetransfer/">storagetransfer</a><br />
<a href="/providers/google/streetviewpublish/">streetviewpublish</a><br />
<a href="/providers/google/tagmanager/">tagmanager</a><br />
<a href="/providers/google/tasks/">tasks</a><br />
<a href="/providers/google/testing/">testing</a><br />
<a href="/providers/google/texttospeech/">texttospeech</a><br />
<a href="/providers/google/toolresults/">toolresults</a><br />
<a href="/providers/google/tpu/">tpu</a><br />
<a href="/providers/google/trafficdirector/">trafficdirector</a><br />
<a href="/providers/google/translate/">translate</a><br />
<a href="/providers/google/vault/">vault</a><br />
<a href="/providers/google/vectortile/">vectortile</a><br />
<a href="/providers/google/verifiedaccess/">verifiedaccess</a><br />
<a href="/providers/google/videointelligence/">videointelligence</a><br />
<a href="/providers/google/vision/">vision</a><br />
<a href="/providers/google/webmasters/">webmasters</a><br />
<a href="/providers/google/websecurityscanner/">websecurityscanner</a><br />
<a href="/providers/google/youtube/">youtube</a><br />
<a href="/providers/google/youtubeAnalytics/">youtubeAnalytics</a><br />
<a href="/providers/google/youtubereporting/">youtubereporting</a><br />
</div>
</div>
