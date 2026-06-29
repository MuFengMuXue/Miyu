# Elasticsearch

From Wikipedia:Elasticsearch:

:Elasticsearch is a search engine based on Lucene. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is developed in Java and is released as open source under the terms of the Apache License.

## Installation
Elasticsearch now requires , see Java.

Install the  package.

## Running
If you do not have a keystore at , you need to create one before starting Elasticsearch:

 # elasticsearch-keystore create

Afterwards, you can start/enable .

Ensure Elasticsearch is running and accessible by using , :
{{hc|curl http://127.0.0.1:9200|2=

{
  "name" : "Sunder",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "*cluster-uuid*",
  "version" : {
    "number" : "2.4.1",
    "build_hash" : "c67dc32e24162035d18d6fe1e952c4cbcbe79d16",
    "build_timestamp" : "2016-09-27T18:57:55Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.2"
  },
  "tagline" : "You Know, for Search"
}

}}

## Configuration
The main Elasticsearch configuration file is well-documented and located at .

* By default Elasticsearch is public accessible, it may be preferred to allow only access on the host instead:

 network.host: 127.0.0.1

* It is possible to use a custom port instead of the default :

 http.port: 9200

You may want to change the default initial and maximum allowed memory usage Reduce from 4g to 2g if you get the Linux Out-Of-Memory error.

You might need to update the [https://www.elastic.co/guide/en/elasticsearch/reference/5.2/vm-max-map-count.html vm.max_map_count system limit:

 # sysctl -w vm.max_map_count=262144

## Usage
Elasticsearch uses a REST API, see Wikipedia:RESTful API for more information.

The quick start section of the Elasticsearch guide should provide you with basic and detailed usage information.

The Elasticsearch server management (document maintenance, performing search, etc.) is usually done by clients, that should provide a seamless integration with the preferred programming language.

Useful tools to manage ElasticSearch instances and clusters like ElasticHQ, Elasticsearch GUI, Kibana and Adminer are also available to simplify management.

## Basic Security
Security is enabled and configured by default in Elasticsearch 8.0 and later.
Elasticsearch provides documentation to set up the mandatory basic security feature.
