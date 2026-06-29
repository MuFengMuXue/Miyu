# OpenSearch

From Wikipedia:OpenSearch (software):

:OpenSearch is a family of software consisting of a search engine (also named OpenSearch), and OpenSearch Dashboards, a data visualization dashboard for that search engine. The software started in 2021 as a fork of Elasticsearch and Kibana, with development led by Amazon Web Services.

## Installation
Install the  package.

Various plugins are listed as optional dependencies which can be installed according to your needs. If you are using  remember to install the corresponding Dashboards plugins.

## Configuration
The main OpenSearch configuration file is well-documented and located at . The official documentation should prove helpful as well.

* By default OpenSearch is public accessible, it may be preferred to allow only access on the host instead:

 network.host: 127.0.0.1

* It is possible to use a custom port instead of the default :

 http.port: 9200

## Usage
If you do not have a keystore at , you need to create one before starting OpenSearch:

 # opensearch-keystore create

Afterwards, you can start/enable .

Ensure OpenSearch is running and accessible by using CURL:

{{hc|$ curl http://127.0.0.1:9200|2=
{
  "name" : "opensearch.example.net",
  "cluster_name" : "opensearch",
  "cluster_uuid" : "TRylpzbsQB-Nk2KgktTQtA",
  "version" : {
    "number" : "7.10.2",
    "build_type" : "tar",
    "build_hash" : "unknown",
    "build_date" : "2022-01-07T15:57:30.358290Z",
    "build_snapshot" : false,
    "lucene_version" : "8.10.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "The OpenSearch Project: https://opensearch.org/"
}
}}

The OpenSearch server management (document maintenance, performing search, etc.) is usually done by clients that should provide a seamless integration with the preferred programming language.

Useful tools to manage OpenSearch instances and clusters like  and  are also available to simplify management.

## Tips and tricks
## Upgrading from Elasticsearch OSS
To upgrade multi-node clusters of Elasticsearch OSS to OpenSearch one should consult the official guide.

For standalone nodes it might suffice to copy any configuration changes and move the index data to its new location:

Stop

 # cp -r /var/lib/elasticsearch/nodes /var/lib/opensearch/

 # chown opensearch:opensearch -R /var/lib/opensearch

Start

## Compatibility with Beats OSS
Beats agents like filebeat are not compatible with OpenSearch in newer versions, the official documentation provides compatibility tables. Versions  and above will not work and all  versions need a workaround in the configuration:

This will make OpenSearch return  as its version number.

Agent versions compatible with the above workaround are available:

*
*
*
*
*
*
