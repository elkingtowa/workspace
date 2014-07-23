Credit to Andrea Mostosi

Big Data Frameworks

Apache Hadoop	
framework for distributed processing. Integrates MapReduce (parallel processing), YARN (job scheduling) and HDFS (distributed file system)

1. Apache Hadoop
Distributed Programming
AddThis Hydra	
Hydra is a distributed data processing and storage system originally developed at AddThis. It ingests streams of data (think log files) and builds trees that are aggregates, summaries, or transformations of the data. These trees can be used by humans to explore (tiny queries), as part of a machine learning pipeline (big queries), or to support live consoles on websites (lots of queries).

1. Github
AMPLab SIMR	
Apache Spark was developed thinking in Apache YARN. However, up to now, it has been relatively hard to run Apache Spark on Hadoop MapReduce v1 clusters, i.e. clusters that do not have YARN installed. Typically, users would have to get permission to install Spark/Scala on some subset of the machines, a process that could be time consuming. SIMR allows anyone with access to a Hadoop MapReduce v1 cluster to run Spark out of the box. A user can run Spark directly on top of Hadoop MapReduce v1 without any administrative rights, and without having Spark or Scala installed on any of the nodes.

1. SIMR on GitHub
Apache Crunch	
is a simple Java API for tasks like joining and data aggregation that are tedious to implement on plain MapReduce. The APIs are especially useful when processing data that does not fit naturally into relational model, such as time series, serialized object formats like protocol buffers or Avro records, and HBase rows and columns. For Scala users, there is the Scrunch API, which is built on top of the Java APIs and includes a REPL (read-eval-print loop) for creating MapReduce pipelines.

1. Website
Apache DataFu	
DataFu provides a collection of Hadoop MapReduce jobs and functions in higher level languages based on it to perform data analysis. It provides functions for common statistics tasks (e.g. quantiles, sampling), PageRank, stream sessionization, and set and bag operations. DataFu also provides Hadoop jobs for incremental data processing in MapReduce. DataFu is a collection of Pig UDFs (including PageRank, sessionization, set operations, sampling, and much more) that were originally developed at LinkedIn.

1. DataFu Apache Incubator
2. LinkedIn DataFu
Apache Gora	
framework for in-memory data model and persistence

1. Apache Gora
Apache Hama	
Apache Top-Level open source project, allowing you to do advanced analytics beyond MapReduce. Many data analysis techniques such as machine learning and graph algorithms require iterative computations, this is where Bulk Synchronous Parallel model can be more effective than “plain” MapReduce.

1. Hama site
Apache MapReduce	
MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. Apache MapReduce was derived from Google MapReduce: Simplified Data Processing on Large Clusters paper. The current Apache MapReduce version is built over Apache YARN Framework. YARN stands for “Yet-Another-Resource-Negotiator”. It is a new framework that facilitates writing arbitrary distributed processing frameworks and applications. YARN’s execution model is more generic than the earlier MapReduce implementation. YARN can run applications that do not follow the MapReduce model, unlike the original Apache Hadoop MapReduce (also called MR1). Hadoop YARN is an attempt to take Apache Hadoop beyond MapReduce for data-processing.

1. Apache MapReduce
2. Google MapReduce paper
3. Writing YARN applications
Apache Pig	
Pig provides an engine for executing data flows in parallel on Hadoop. It includes a language, Pig Latin, for expressing these data flows. Pig Latin includes operators for many of the traditional data operations (join, sort, filter, etc.), as well as the ability for users to develop their own functions for reading, processing, and writing data. Pig runs on Hadoop. It makes use of both the Hadoop Distributed File System, HDFS, and Hadoop’s processing system, MapReduce.

1. pig.apache.org/
2. 2.Pig examples by Alan Gates
Apache S4	
S4 is a general-purpose, distributed, scalable, fault-tolerant, pluggable platform that allows programmers to easily develop applications for processing continuous unbounded streams of data.

1. Apache S4
Apache Spark	
Data analytics cluster computing framework originally developed in the AMPLab at UC Berkeley. Spark fits into the Hadoop open-source community, building on top of the Hadoop Distributed File System (HDFS). However, Spark provides an easier to use alternative to Hadoop MapReduce and offers performance up to 10 times faster than previous generation systems like Hadoop MapReduce for certain applications.

1. Apache Incubator Spark
Apache Spark Streaming	
framework for stream processing, part of Spark

1. Apache Spark Streaming
Apache Storm	
Storm is a complex event processor and distributed computation framework written predominantly in the Clojure programming language. Is a distributed real-time computation system for processing fast, large streams of data. Storm is an architecture based on master-workers paradigma. So a Storm cluster mainly consists of a master and worker nodes, with coordination done by Zookeeper.

1. Storm Project/
2. Storm-on-YARN
Apache Tez	
Tez is a proposal to develop a generic application which can be used to process complex data-processing task DAGs and runs natively on Apache Hadoop YARN.

1. Apache Tez
Apache Twill	
Twill is an abstraction over Apache Hadoop® YARN that reduces the complexity of developing distributed applications, allowing developers to focus more on their business logic. Twill uses a simple thread-based model that Java programmers will find familiar. YARN can be viewed as a compute fabric of a cluster, which means YARN applications like Twill will run on any Hadoop 2 cluster.

1. Apache Twill Incubator
Cascalog	
data processing and querying library

1. Cascalog
Cheetah	
High Performance, Custom Data Warehouse on Top of MapReduce

1. Paper
Concurrent Cascading	
Application framework for Java developers to simply develop robust Data Analytics and Data Management applications on Apache Hadoop.

1. Cascanding
Damballa Parkour	
Library for develop MapReduce programs using the LISP like language Clojure. Parkour aims to provide deep Clojure integration for Hadoop. Programs using Parkour are normal Clojure programs, using standard Clojure functions instead of new framework abstractions. Programs using Parkour are also full Hadoop programs, with complete access to absolutely everything possible in raw Java Hadoop MapReduce.

1. Parkour GitHub Project
Datasalt Pangool	
A new MapReduce paradigm. A new API for MR jobs, in higher level than Java.

DataTorrent StrAM	
real-time engine is designed to enable distributed, asynchronous, real time in-memory big-data computations in as unblocked a way as possible, with minimal overhead and impact on performance.

1. 
Facebook Corona	
“The next version of Map-Reduce” from Facebook, based in own fork of Hadoop. The current Hadoop implementation of the MapReduce technique uses a single job tracker, which causes scaling issues for very large data sets. The Apache Hadoop developers have been creating their own next-generation MapReduce, called YARN, which Facebook engineers looked at but discounted because of the highly-customised nature of the company’s deployment of Hadoop and HDFS. Corona, like YARN, spawns multiple job trackers (one for each job, in Corona’s case).

Facebook Peregrine	
Map Reduce framework

1. Facebook Peregrine
Facebook Scuba	
distributed in-memory datastore

Google MapReduce	
map reduce framework

Google MillWheel	
fault tolerant stream processing framework

HadoopDB	
hybrid of MapReduce and DBMS

1. HadoopDB
JAQL	
JAQL is a functional, declarative programming language designed especially for working with large volumes of structured, semi-structured and unstructured data. As its name implies, a primary use of JAQL is to handle data stored as JSON documents, but JAQL can work on various types of data. For example, it can support XML, comma-separated values (CSV) data and flat files. A “SQL within JAQL” capability lets programmers work with structured SQL data while employing a JSON data model that’s less restrictive than its Structured Query Language counterparts.

1. JAQL in Google Code
2. What is Jaql? by IBM
Kite	
is a set of libraries, tools, examples, and documentation focused on making it easier to build systems on top of the Hadoop ecosystem.

1. Website
Metamarkers Druid	
Realtime analytical data store.

1. Druid
Netflix PigPen	
PigPen is map-reduce for Clojure whiche compiles to Apache Pig. Clojure is dialect of the Lisp programming language created by Rich Hickey, so is a functional general-purpose language, and runs on the Java Virtual Machine, Common Language Runtime, and JavaScript engines. In PigPen there are no special user defined functions (UDFs). Define Clojure functions, anonymously or named, and use them like you would in any Clojure program. This tool is open sourced by Netflix, Inc. the American provider of on-demand Internet streaming media.

1. PigPen on GitHub
Nokia Disco	
MapReduce framework developed by Nokia

1. Nokia Disco
Pydoop	
Pydoop is a Python MapReduce and HDFS API for Hadoop, built upon the C++ Pipes and the C libhdfs APIs, that allows to write full-fledged MapReduce applications with HDFS access. Pydoop has several advantages over Hadoop’s built-in solutions for Python programming, i.e., Hadoop Streaming and Jython: being a CPython package, it allows you to access all standard library and third party modules, some of which may not be available.

1. SF Pydoop site
2. Pydoop GitHub Project
Stratosphere	
Stratosphere is a general purpose cluster computing framework. It is compatible to the Hadoop ecosystem: Stratosphere can access data stored in HDFS and runs with Hadoop’s new cluster manager YARN. The common input formats of Hadoop are supported as well. Stratosphere does not use Hadoop’s MapReduce implementation: it is a completely new system that brings its own runtime. The new runtime allows to define more advanced operations that include more transformations than just map and reduce. Additionally, Stratosphere allows to express analysis jobs using advanced data flow graphs, which are able to resemble common data analysis task more naturally.

1. Stratosphere site
Twitter Scalding	
Scala library for Map Reduce jobs, built on Cascading

1. Twitter Scalding
Twitter Summingbird	
a system that aims to mitigate the tradeoffs between batch processing and stream processing by combining them into a hybrid system. In the case of Twitter, Hadoop handles batch processing, Storm handles stream processing, and the hybrid system is called Summingbird.

1. Summingbird
Distributed Filesystem
Apache HDFS	
The Hadoop Distributed File System (HDFS) offers a way to store large files across multiple machines. Hadoop and HDFS was derived from Google File System (GFS) paper. Prior to Hadoop 2.0.0, the NameNode was a single point of failure (SPOF) in an HDFS cluster. With Zookeeper the HDFS High Availability feature addresses this problem by providing the option of running two redundant NameNodes in the same cluster in an Active/Passive configuration with a hot standby.

1. hadoop.apache.org
2. Google FileSystem - GFS Paper
3. Cloudera Why HDFS
4. Hortonworks Why HDFS
Ceph Filesystem	
Ceph is a free software storage platform designed to present object, block, and file storage from a single distributed computer cluster. Ceph’s main goals are to be completely distributed without a single point of failure, scalable to the exabyte level, and freely-available. The data is replicated, making it fault tolerant. The problem right now is Ceph currently requires Hadoop 1.1.X stable series.

1. Ceph Filesystem site
2. Ceph and Hadoop
3. HADOOP-6253
Facebook Haystack	
object storage system

1. Facebook Haystack
Google Colossus	
distributed filesystem (GFS2)

Google GFS	
distributed filesystem

Google Megastore	
scalable, highly available storage

GridGain	
GridGain is open source project licensed under Apache 2.0. One of the main pieces of this platform is the In-Memory Apache Hadoop Accelerator which aims to accelerate HDFS and Map/Reduce by bringing both, data and computations into memory. This work is done with the GGFS - Hadoop compliant in-memory file system. For I/O intensive jobs GridGain GGFS offers performance close to 100x faster than standard HDFS. Paraphrasing Dmitriy Setrakyan from GridGain Systems talking about GGFS regarding Tachyon: GGFS allows read-through and write-through to/from underlying HDFS or any other Hadoop compliant file system with zero code change. Essentially GGFS entirely removes ETL step from integration.GGFS has ability to pick and choose what folders stay in memory, what folders stay on disc, and what folders get synchronized with underlying (HD)FS either synchronously or asynchronously. GridGain is working on adding native MapReduce component which will provide native complete Hadoop integration without changes in API, like Spark currently forces you to do. Essentially GridGain MR+GGFS will allow to bring Hadoop completely or partially in-memory in Plug-n-Play fashion without any API changes.

1. GridGain site
Lustre file system	
The Lustre filesystem is a high-performance distributed filesystem intended for larger network and high-availability environments. Traditionally, Lustre is configured to manage remote data storage disk devices within a Storage Area Network (SAN), which is two or more remotely attached disk devices communicating via a Small Computer System Interface (SCSI) protocol. This includes Fibre Channel, Fibre Channel over Ethernet (FCoE), Serial Attached SCSI (SAS) and even iSCSI.

1. wiki.lustre.org/
2. Hadoop with Lustre
3. Intel HPC Hadoop
Quantcast File System QFS	
(QFS) is an open-source distributed file system software package for large-scale MapReduce or other batch-processing workloads. It was designed as an alternative to Apache Hadoop’s HDFS, intended to deliver better performance and cost-efficiency for large-scale processing clusters. It is written in C++ and has fixed-footprint memory management. QFS uses Reed-Solomon error correction as method for assuring reliable access to data.

1. QFS site
2. GitHub QFS
3. HADOOP-8885
Red Hat GlusterFS	
GlusterFS is a scale-out network-attached storage file system. GlusterFS was developed originally by Gluster, Inc., then by Red Hat, Inc., after their purchase of Gluster in 2011. In June 2012, Red Hat Storage Server was announced as a commercially-supported integration of GlusterFS with Red Hat Enterprise Linux. Gluster File System, known now as Red Hat Storage Server.

1. www.gluster.org
2. Red Hat Hadoop Plugin
Tachyon	
Tachyon is an memory distributed file system. By storing the file-system contents in the main memory of all cluster nodes, the system achieves higher throughput than traditional disk-based storage systems like HDFS.

1. Tachyon site
Column Data Model
Actian Vector	
column-oriented analytic database

1. Actian website
Apache Accumulo	
Distributed key/value store is a robust, scalable, high performance data storage and retrieval system. Apache Accumulo is based on Google’s BigTable design and is built on top of Apache Hadoop, Zookeeper, and Thrift. Accumulo is software created by the NSA with security features.

1. Apache Accumulo
Apache Cassandra	
Distributed Non-SQL DBMS, it’s a BDDB. MR can retrieve data from Cassandra. This BDDB can run without HDFS, or on-top of HDFS (DataStax fork of Cassandra). HBase and its required supporting systems are derived from what is known of the original Google BigTable and Google File System designs (as known from the Google File System paper Google published in 2003, and the BigTable paper published in 2006). Cassandra on the other hand is a recent open source fork of a standalone database system initially coded by Facebook, which while implementing the BigTable data model, uses a system inspired by Amazon’s Dynamo for storing data (in fact much of the initial development work on Cassandra was performed by two Dynamo engineers recruited to Facebook from Amazon).

1. Apache Cassandra
Apache HBase	
Google BigTable Inspired. Non-relational distributed database. Ramdom, real-time r/w operations in column-oriented very large tables (BDDB: Big Data Data Base). It’s the backing system for MR jobs outputs. It’s the Hadoop database. It’s for backing Hadoop MapReduce jobs with Apache HBase tables

1. Apache HBase
C-Store	
column oriented DBMS

1. Website
Facebook HydraBase	
Evolution of HBase made by Facebook

1. Blog Post on Facebook engineer
Google BigTable	
column-oriented distributed datastore

1. Google BigTable
Google Cloud Datastore	
is a fully managed, schemaless database for storing non-relational data built on top of Google’s BigTable infrastructure

1. Google Cloud Datastore site
2. Google App Engine Datastore
3. Matering Datastore
Hypertable	
Database system inspired by publications on the design of Google’s BigTable. The project is based on experience of engineers who were solving large-scale data-intensive tasks for many years. Hypertable runs on top of a distributed file system such as the Apache Hadoop DFS, GlusterFS, or the Kosmos File System (KFS). It is written almost entirely in C++. Sposored by Baidu the Chinese search engine.

1. HyperTable
InfiniDB	
is accessed through a MySQL interface and use massive parallel processing to parallelize queries

1. Website
MonetDB	
column store database

1. Website
OhmData C5	
improved version of HBase

1. OhmData website
Parquet	
columnar storage format for Hadoop.

1. Parquet
Twitter Manhattan	
real-time, multi-tenant distributed database for Twitter scale

1. Blog post on Twitter Engineering blog
Vertica	
The grid-based, column-oriented, Vertica Analytics Platform is designed to manage large, fast-growing volumes of data and provide very fast query performance when used for data warehouses and other query-intensive applications. The product claims to drastically improve query performance over traditional relational database systems, provide high-availability, and petabyte scalability on commodity enterprise servers.

1. Website
Document Data Model
Crate Data	
is an open source massively scalable data store. It requires zero administration.

1. Website
Facebook Apollo	
Facebook’s Paxos-like NoSQL database

1. infoQ post
jumboDB	
document oriented datastore over Hadoop

1. jumboDB
LinkedIn Espresso	
horizontally scalable document-oriented NoSQL data store

1. LinkedIn Espresso
MarkLogic	
Schema-agnostic Enterprise NoSQL database technology

1. Website
MongoDB	
Document-oriented database system. It is part of the NoSQL family of database systems. Instead of storing data in tables as is done in a “classical” relational database, MongoDB stores structured data as JSON-like documents

1. Mongodb site
RethinkDB	
RethinkDB is built to store JSON documents, and scale to multiple machines with very little effort. It has a pleasant query language that supports really useful queries like table joins and group by, and is easy to setup and learn.

1. RethinkDB site
Key-value Data Model
Amazon DynamoDB	
distributed key/value store, implementation of Dynamo

1. Amazon DynamoDB
Edis	
Edis is a protocol-compatible Server replacement for Redis, written in Erlang. Edis’s goal is to be a drop-in replacement for Redis when persistence is more important than holding the dataset in-memory. Edis (currently) uses Google’s leveldb as a backend. Future plans call for a multi-master clustering model. Near term goals are to act as a read-slave for existing Redis servers.

1. Website
ElephantDB	
Distributed database specialized in exporting data from Hadoop

1. ElephantDB
EventStore	
An open-source, functional database with support for Complex Event Processing. It provides a persistence engine for applications using event-sourcing, or for storing time-series data. Event Store is written in C#, C++ for the server which runs on Mono or the .NET CLR, on Linux or Windows. Applications using Event Store can be written in JavaScript.

1. EventStore
LinkedIn Krati	
is a simple persistent data store with very low latency and high throughput. It is designed for easy integration with read-write-intensive applications with little effort in tuning configuration, performance and JVM garbage collection.

1. 
Linkedin Voldemort	
Distributed data store that is designed as a key-value store used by LinkedIn for high-scalability storage.

1. LinkedIn Voldemort
OpenTSDB	
OpenTSDB is a distributed, scalable Time Series Database (TSDB) written on top of HBase. OpenTSDB was written to address a common need: store, index and serve metrics collected from computer systems (network gear, operating systems, applications) at a large scale, and make this data easily accessible and graphable.

1. OpenTSDB site
Redis DataBase	
Redis is an open-source, networked, in-memory, key-value data store with optional durability. It is written in ANSI C. In its outer layer, the Redis data model is a dictionary which maps keys to values. One of the main differences between Redis and other structured storage systems is that Redis supports not only strings, but also abstract data types. Sponsored by Pivotal and VMWare. It’s BSD licensed.

1. Redis.io
Storehaus	
library to work with asynchronous key value stores, by Twitter

1. Storehaus
Graph Data Model
Apache Giraph	
Apache Giraph is an iterative graph processing system built for high scalability. For example, it is currently used at Facebook to analyze the social graph formed by users and their connections. Giraph originated as the open-source counterpart to Pregel, the graph processing architecture developed at Google

1. Apache Giraph
Apache Spark Bagel	
implementation of Pregel, part of Spark

1. Apache Spark Bagel
ArangoDB	
An open-source database with a flexible data model for documents, graphs, and key-values. Build high performance applications using a convenient sql-like query language or JavaScript extensions.

1. ArangoDB site
Facebook TAO	
TAO is the distributed data store that is widely used at facebook to store and serve the social graph. The entire architecture is highly read optimized, supports a graph data model and works across multiple geographical regions.

1. Post about TAO
Google Pregel	
graph processing framework

GraphLab PowerGraph	
a core C++ GraphLab API and a collection of high-performance machine learning and data mining toolkits built on top of the GraphLab API. In addition, we are actively developing new interfaces to allow users to leverage the GraphLab API from other languages and technologies.

1. Graphlab website
GraphX	
A Resilient Distributed Graph System on Spark

1. GraphX
Intel GraphBuilder	
library which provides tools to construct large-scale graphs on top of Apache Hadoop

Neo4j	
An open-source graph database writting entirely in Java. It is an embedded, disk-based, fully transactional Java persistence engine that stores data structured in graphs rather than in tables.

1. Neo4j site
OrientDB	
It is an Open Source NoSQL DBMS with the features of both Document and Graph DBMSs. Written in Java, it is incredibly fast: it can store up to 150,000 records per second on common hardware.

1. OrientDB site
Phoebus	
framework for large scale graph processing

1. Phoebus
Titan	
distributed graph database, built over Cassandra

1. Titan
Twitter FlockDB	
distribuited graph database

1. Twitter FlockDB
NewSQL Databases
Amazon RedShift	
data warehouse service, based on PostgreSQL

1. Amazon RedShift
BayesDB	
BayesDB, a Bayesian database table, lets users query the probable implications of their tabular data as easily as an SQL database lets them query the data itself. Using the built-in Bayesian Query Language (BQL), users with no statistics training can solve basic data science problems, such as detecting predictive relationships between variables, inferring missing values, simulating probable observations, and identifying statistically similar database entries.

1. BayesDB site
FoundationDB	
distributed database, inspired by F1, aquired Akiban server

1. FoundationDB
2. Akiban Server
Google F1	
distributed SQL database built on Spanner

Google Spanner	
globally distributed semi-relational database

H-Store	
is an experimental main-memory, parallel database management system that is optimized for on-line transaction processing (OLTP) applications. It is a highly distributed, row-store-based relational database that runs on a cluster on shared-nothing, main memory executor nodes.

1. Brown project website
Haeinsa	
Haeinsa is linearly scalable multi-row, multi-table transaction library for HBase. Use Haeinsa if you need strong ACID semantics on your HBase cluster. Is based on Google Perlcoator concept.

HandlerSocket	
HandlerSocket is a NoSQL plugin for MySQL/MariaDB (the storage engine of MySQL). It works as a daemon inside the mysqld process, accepting TCP connections, and executing requests from clients. HandlerSocket does not support SQL queries. Instead, it supports simple CRUD operations on tables. HandlerSocket can be much faster than mysqld/libmysql in some cases because it has lower CPU, disk, and network overhead.

InfiniSQL	
infinity scalable RDBMS

1. InfiniSQL
InfluxDB	
InfluxDB is an open source distributed time series database with no external dependencies. It’s useful for recording metrics, events, and performing analytics. It has a built-in HTTP API so you don’t have to write any server side code to get up and running. InfluxDB is designed to be scalable, simple to install and manage, and fast to get data in and out. It aims to answer queries in real-time. That means every data point is indexed as it comes in and is immediately available in queries that should return in

MemSQL	
in memory SQL database witho optimized columnar storage on flash

1. MemSQL site
NuoDB	
SQL/ACID compliant distributed database

1. NuoDB
Postgres-XL	
Scalable Open Source PostgreSQL-based Database Cluster

1. Website
SenseiDB	
Open-source, distributed, realtime, semi-structured database. Some Features: Full-text search, Fast realtime updates, Structured and faceted search, BQL: SQL-like query language, Fast key-value lookup, High performance under concurrent heavy update and query volumes, Hadoop integration

1. SenseiDB site
Sky	
Sky is an open source database used for flexible, high performance analysis of behavioral data. For certain kinds of data such as clickstream data and log data, it can be several orders of magnitude faster than traditional approaches such as SQL databases or Hadoop.

1. SkyDB site
SymmetricDS	
SymmetricDS is open source software for both file and database synchronization with support for multi-master replication, filtered synchronization, and transformation across the network in a heterogeneous environment. It supports multiple subscribers with one direction or bi-directional, asynchronous data replication. It uses web and database technologies to replicate data as a scheduled or near real-time operation. The software was designed to scale for a large number of nodes, work across low-bandwidth connections, and withstand periods of network outage. It works with most operating systems, file systems, and databases, including Oracle, MySQL, MariaDB, PostgreSQL, MS SQL Server (including Azure), IBM DB2, H2, HSQLDB, Derby, Firebird, Interbase, Informix, Greenplum, SQLite (including Android), Sybase ASE, and Sybase ASA (SQL Anywhere) databases.

1. SymmetricDS
SQL-like processing
AMPLAB Shark	
Shark is a large-scale data warehouse system for Spark designed to be compatible with Apache Hive. It can execute Hive QL queries up to 100 times faster than Hive without any modification to the existing data or queries. Shark supports Hive’s query language, metastore, serialization formats, and user-defined functions, providing seamless integration with existing Hive deployments and a familiar, more powerful option for new ones. Shark is built on top of Spark

1. AMPLAB on GitHub Shark
Apache Drill	
Drill is the open source version of Google’s Dremel system which is available as an infrastructure service called Google BigQuery. In recent years open source systems have emerged to address the need for scalable batch processing (Apache Hadoop) and stream processing (Storm, Apache S4). Apache Hadoop, originally inspired by Google’s internal MapReduce system, is used by thousands of organizations processing large-scale datasets. Apache Hadoop is designed to achieve very high throughput, but is not designed to achieve the sub-second latency needed for interactive data analysis and exploration. Drill, inspired by Google’s internal Dremel system, is intended to address this need

1. Apache Drill
Apache HCatalog	
HCatalog’s table abstraction presents users with a relational view of data in the Hadoop Distributed File System (HDFS) and ensures that users need not worry about where or in what format their data is stored. Right now HCatalog is part of Hive. Only old versions are separated for download.

1. Apache HCatalog
Apache Hive	
Data Warehouse infrastructure developed by Facebook. Data summarization, query, and analysis. It’s provides SQL-like language (not SQL92 compliant): HiveQL.

1. Apache Hive
Apache Phoenix	
Apache Phoenix is a SQL skin over HBase delivered as a client-embedded JDBC driver targeting low latency queries over HBase data. Apache Phoenix takes your SQL query, compiles it into a series of HBase scans, and orchestrates the running of those scans to produce regular JDBC result sets. The table metadata is stored in an HBase table and versioned, such that snapshot queries over prior versions will automatically use the correct schema. Direct use of the HBase API, along with coprocessors and custom filters, results in performance on the order of milliseconds for small queries, or seconds for tens of millions of rows.

1. Apache Phoenix site
BlinkDB	
massively parallel, approximate query engine

1. BlinkDB
Cloudera Impala	
The Apache-licensed Impala project brings scalable parallel database technology to Hadoop, enabling users to issue low-latency SQL queries to data stored in HDFS and Apache HBase without requiring data movement or transformation. It’s a Google Dremel clone (Big Query google).

1. Cloudera Impala
Concurrent Lingual	
Open source project enabling fast and simple Big Data application development on Apache Hadoop. project that delivers ANSI-standard SQL technology to easily build new and integrate existing applications onto Hadoop

1. Cascading Lingual
Datasalt Splout SQL	
Splout allows serving an arbitrarily big dataset with high QPS rates and at the same time provides full SQL query syntax.

Facebook PrestoDB	
Facebook has open sourced Presto, a SQL engine it says is on average 10 times faster than Hive for running queries across large data sets stored in Hadoop and elsewhere.

1. Facebook PrestoDB
Google BigQuery	
framework for interactive analysis, implementation of Dremel

1. Google BigQuery
Pivotal HAWQ	
SQL-like data warehouse system for Hadoop

1. Pivotal HAWQ
Spark Catalyst	
Catalyst is a Query Optimization Framework for Spark and Shark

1. Github sub page
SparkSQL	
Manipulating Structured Data Using Spark

1. Databricks blog post
Splice Machine	
a full-featured SQL-on-Hadoop RDBMS with ACID transactions

1. Website
Stinger	
interactive query for Hive

1. Stinger
Tajo	
Tajo is a distributed data warehouse system on Hadoop that provides low-latency and scalable ad-hoc queries and ETL on large-data sets stored on HDFS and other data sources.

1. Tajo site
Data Ingestion
Amazon Kinesis	
Real-time processing of streaming data at massive scale

1. Amazon Kinesis
Apache Chukwa	
Large scale log aggregator, and analytics.

1. Apache Chukwa
Apache Flume	
Un-structured data agregator to HDFS.

1. Apache Flume
Apache Kafka	
Distributed publish-subscribe system for processing large amounts of streaming data. Kafka is a Message Queue developed by LinkedIn that persists messages to disk in a very performant manner. Because messages are persisted, it has the interesting ability for clients to rewind a stream and consume the messages again. Another upside of the disk persistence is that bulk importing the data into HDFS for offline analysis can be done very quickly and efficiently. Storm, developed by BackType (which was acquired by Twitter a year ago), is more about transforming a stream of messages into new streams.

1. Apache Kafka
Apache Samza	
Apache Samza is a distributed stream processing framework. It uses Apache Kafka for messaging, and Apache Hadoop YARN to provide fault tolerance, processor isolation, security, and resource management. Developed by http://www.linkedin.com/in/jaykreps Linkedin.

1. Apache Samza
Apache Sqoop	
System for bulk data transfer between HDFS and structured datastores as RDBMS. Like Flume but from HDFS to RDBMS.

1. Apache Sqoop
Cloudera Morphline	
Cloudera Morphlines is a new open source framework that reduces the time and skills necessary to integrate, build, and change Hadoop processing applications that extract, transform, and load data into Apache Solr, Apache HBase, HDFS, enterprise data warehouses, or analytic online dashboards.

Facebook Scribe	
Log agregator in real-time. It’s a Apache Thrift Service.

1. Facebook Scribe
Fluentd	
tool to collect events and logs

1. Fluentd
HIHO	
This project is a framework for connecting disparate data sources with the Apache Hadoop system, making them interoperable. HIHO connects Hadoop with multiple RDBMS and file systems, so that data can be loaded to Hadoop and unloaded from Hadoop

Kestrel	
distributed message queue system

1. Kestrel
LinkedIn Databus	
stream of change capture events for a database

1. LinkedIn Databus
LinkedIn Kamikaze	
utility package for compressing sorted integer arrays

1. LinkedIn Kamikaze
LinkedIn White Elephant	
log aggregator and dashboard

1. LinkedIn White Elephant
Netflix Suro	
Suro has its roots in Apache Chukwa, which was initially adopted by Netflix. Is a log agregattor like Storm, Samza.

Pinterest Secor	
is a service implementing Kafka log persistance

1. Github
Service Programming
Akka Toolkit	
Akka is an open-source toolkit and runtime simplifying the construction of concurrent applications on the Java platform.

Apache Avro	
Apache Avro is a framework for modeling, serializing and making Remote Procedure Calls (RPC). Avro data is described by a schema, and one interesting feature is that the schema is stored in the same file as the data it describes, so files are self-describing. Avro does not require code generation. This framework can compete with other similar tools like: Apache Thrift, Google Protocol Buffers, ZeroC ICE, and so on.

1. Apache Avro
Apache Curator	
Curator is a set of Java libraries that make using Apache ZooKeeper much easier.

Apache Karaf	
Apache Karaf is an OSGi runtime that runs on top of any OSGi framework and provides you a set of services, a powerful provisioning concept, an extensible shell & more.

Apache Thrift	
A cross-language RPC framework for service creations. It’s the service base for Facebook technologies (the original Thrift contributor). Thrift provides a framework for developing and accessing remote services. It allows developers to create services that can be consumed by any application that is written in a language that there are Thrift bindings for. Thrift manages serialization of data to and from a service, as well as the protocol that describes a method invocation, response, etc. Instead of writing all the RPC code – you can just get straight to your service logic. Thrift uses TCP and so a given service is bound to a particular port.

1. Apache Thrift
Apache Zookeeper	
It’s a coordination service that gives you the tools you need to write correct distributed applications. ZooKeeper was developed at Yahoo! Research. Several Hadoop projects are already using ZooKeeper to coordinate the cluster and provide highly-available distributed services. Perhaps most famous of those are Apache HBase, Storm, Kafka. ZooKeeper is an application library with two principal implementations of the APIs—Java and C—and a service component implemented in Java that runs on an ensemble of dedicated servers. Zookeeper is for building distributed systems, simplifies the development process, making it more agile and enabling more robust implementations. Back in 2006, Google published a paper on “Chubby”, a distributed lock service which gained wide adoption within their data centers. Zookeeper, not surprisingly, is a close clone of Chubby designed to fulfill many of the same roles for HDFS and other Hadoop infrastructure.

1. Apache Zookeeper
2. Google Chubby paper
Google Chubby	
a lock service for loosely-coupled distributed systems

1. Paper
Linkedin Norbert	
Norbert is a library that provides easy cluster management and workload distribution. With Norbert, you can quickly distribute a simple client/server architecture to create a highly scalable architecture capable of handling heavy traffic. Implemented in Scala, Norbert wraps ZooKeeper, Netty and uses Protocol Buffers for transport to make it easy to build a cluster aware application. A Java API is provided and pluggable load balancing strategies are supported with round robin and consistent hash strategies provided out of the box.

1. Linedin Project
2. GitHub source code
OpenMPI	
message passing framework

1. OpenMPI
Serf	
decentralized solution for service discovery and orchestration

1. Serf
Spring XD	
Spring XD (Xtreme Data) is a evolution of Spring Java application development framework to help Big Data Applications by Pivotal. SpringSource was the company created by the founders of the Spring Framework. SpringSource was purchased by VMware where it was maintained for some time as a separate division within VMware. Later VMware, and its parent company EMC Corporation, formally created a joint venture called Pivotal. Spring XD is more than development framework library, is a distributed, and extensible system for data ingestion, real time analytics, batch processing, and data export. It could be considered as alternative to Apache Flume/Sqoop/Oozie in some scenarios. Spring XD is part of Pivotal Spring for Apache Hadoop (SHDP). SHDP, integrated with Spring, Spring Batch and Spring Data are part of the Spring IO Platform as foundational libraries. Building on top of, and extending this foundation, the Spring IO platform provides Spring XD as big data runtime. Spring for Apache Hadoop (SHDP) aims to help simplify the development of Hadoop based applications by providing a consistent configuration and API across a wide range of Hadoop ecosystem projects such as Pig, Hive, and Cascading in addition to providing extensions to Spring Batch for orchestrating Hadoop based workflows.

1. Spring XD on GitHub
Twitter Elephant Bird	
Elephant Bird is a project that provides utilities (libraries) for working with LZOP-compressed data. It also provides a container format that supports working with Protocol Buffers, Thrift in MapReduce, Writables, Pig LoadFuncs, Hive SerDe, HBase miscellanea. This open source library is massively used in Twitter.

1. Elephant Bird GitHub
Twitter Finagle	
Finagle is an asynchronous network stack for the JVM that you can use to build asynchronous Remote Procedure Call (RPC) clients and servers in Java, Scala, or any JVM-hosted language.

Scheduling
Apache Aurora	
is a service scheduler that runs on top of Apache Mesos

1. Apache Incubator
Apache Falcon	
Apache™ Falcon is a data management framework for simplifying data lifecycle management and processing pipelines on Apache Hadoop®. It enables users to configure, manage and orchestrate data motion, pipeline processing, disaster recovery, and data retention workflows. Instead of hard-coding complex data lifecycle capabilities, Hadoop applications can now rely on the well-tested Apache Falcon framework for these functions. Falcon’s simplification of data management is quite useful to anyone building apps on Hadoop. Data Management on Hadoop encompasses data motion, process orchestration, lifecycle management, data discovery, etc. among other concerns that are beyond ETL. Falcon is a new data processing and management platform for Hadoop that solves this problem and creates additional opportunities by building on existing components within the Hadoop ecosystem (ex. Apache Oozie, Apache Hadoop DistCp etc.) without reinventing the wheel.

1. Apache Falcon
Apache Oozie	
Workflow scheduler system for MR jobs using DAGs (Direct Acyclical Graphs). Oozie Coordinator can trigger jobs by time (frequency) and data availabilit

1. Apache Oozie
Chronos	
distributed and fault-tolerant scheduler

1. Chronos
Linkedin Azkaban	
Hadoop workflow management. A batch job scheduler can be seen as a combination of the cron and make Unix utilities combined with a friendly UI.

1. LinkedIn Azkaban
Sparrow	
Sparrow is a high throughput, low latency, and fault-tolerant distributed cluster scheduler. Sparrow is designed for applications that require resource allocations frequently for very short jobs, such as analytics frameworks. Sparrow schedules from a distributed set of schedulers that maintain no shared state. Instead, to schedule a job, a scheduler obtains intantaneous load information by sending probes to a subset of worker machines. The scheduler places the job’s tasks on the least loaded of the probed workers. This technique allows Sparrow to schedule in milliseconds, two orders of magnitude faster than existing approaches. Sparrow also handles failures: if a scheduler fails, a client simply directs scheduling requests to an alternate scheduler

1. Github
2. Paper
Machine Learning
Apache Mahout	
Machine learning library and math library, on top of MapReduce.

1. Apache Mahout
Cloudera Oryx	
The Oryx open source project provides simple, real-time large-scale machine learning / predictive analytics infrastructure. It implements a few classes of algorithm commonly used in business applications: collaborative filtering / recommendation, classification / regression, and clustering.

1. Oryx at GitHub
2. Cloudera forum for Machine Learning
Concurrent Pattern	
Machine Learning for Cascading on Apache Hadoop through an API, and standards based PMML

1. Cascading Pattern
etcML	
text classification with machine learning

1. 
Etsy Conjecture	
Conjecture is a framework for building machine learning models in Hadoop using the Scalding DSL. The goal of this project is to enable the development of statistical models as viable components in a wide range of product settings. Applications include classification and categorization, recommender systems, ranking, filtering, and regression (predicting real-valued numbers). Conjecture has been designed with a primary emphasis on flexibility and can handle a wide variety of inputs. Integration with Hadoop and scalding enable seamless handling of extremely large data volumes, and integration with established ETL processes. Predicted labels can either be consumed directly by the web stack using the dataset loader, or models can be deployed and consumed by live web code. Currently, binary classification (assigning one of two possible labels to input data points) is the most mature component of the Conjecture package.

1. Github
H2O	
statistical, machine learning and math runtime for Hadoop

1. H2O
MLbase	
distributed machine learning libraries for the BDAS stack

1. MLbase
PredictionIO	
machine learning server buit on Hadoop, Mahout and Cascading

1. PredictionIO
Spark MLlib	
a Spark implementation of some common machine learning (ML) functionality

1. Spark Documentation
Vowpal Wabbit	
learning system sponsored by Microsoft and Yahoo!

1. Vowpal Wabbit
WEKA	
Weka (Waikato Environment for Knowledge Analysis) is a popular suite of machine learning software written in Java, developed at the University of Waikato, New Zealand. Weka is free software available under the GNU General Public License.

Bechmarking
Apache Hadoop Benchmarking	
There are two main JAR files in Apache Hadoop for benchmarking. This JAR are micro-benchmarks for testing particular parts of the infrastructure, for instance TestDFSIO analyzes the disk system, TeraSort evaluates MapReduce tasks, WordCount measures cluster performance, etc. Micro-Benchmarks are packaged in the tests and exmaples JAR files, and you can get a list of them, with descriptions, by invoking the JAR file with no arguments. With regards Apache Hadoop 2.2.0 stable version we have available the following JAR files for test, examples and benchmarking. The Hadoop micro-benchmarks, are bundled in this JAR files: hadoop-mapreduce-examples-2.2.0.jar, hadoop-mapreduce-client-jobclient-2.2.0-tests.jar.

1. MAPREDUCE-3561 umbrella ticket to track all the issues related to performance
Berkeley SWIM Benchmark	
The SWIM benchmark (Statistical Workload Injector for MapReduce), is a benchmark representing a real-world big data workload developed by University of California at Berkley in close cooperation with Facebook. This test provides rigorous measurements of the performance of MapReduce systems comprised of real industry workloads.

1. GitHub SWIN
Intel HiBench	
HiBench is a Hadoop benchmark suite.

PUMA Benchmarking	
Benchmark suite which represents a broad range of MapReduce applications exhibiting application characteristics with high/low computation and high/low shuffle volumes. There are a total of 13 benchmarks, out of which Tera-Sort, Word-Count, and Grep are from Hadoop distribution. The rest of the benchmarks were developed in-house and are currently not part of the Hadoop distribution. The three benchmarks from Hadoop distribution are also slightly modified to take number of reduce tasks as input from the user and generate final time completion statistics of jobs.

1. MAPREDUCE-5116
2. Faraz Ahmad researcher
3. PUMA Docs
Yahoo Gridmix3	
Hadoop cluster benchmarking from Yahoo engineer team.

Security
Apache Knox Gateway	
System that provides a single point of secure access for Apache Hadoop clusters. The goal is to simplify Hadoop security for both users (i.e. who access the cluster data and execute jobs) and operators (i.e. who control access and manage the cluster). The Gateway runs as a server (or cluster of servers) that serve one or more Hadoop clusters.

Apache Sentry	
Sentry is the next step in enterprise-grade big data security and delivers fine-grained authorization to data stored in Apache Hadoop™. An independent security module that integrates with open source SQL query engines Apache Hive and Cloudera Impala, Sentry delivers advanced authorization controls to enable multi-user applications and cross-functional processes for enterprise data sets. Sentry was a Cloudera development.

System Deployment
Apache Ambari	
Intuitive, easy-to-use Hadoop management web UI backed by its RESTful APIs. Apache Ambari was donated by Hortonworks team to the ASF. It’s a powerful and nice interface for Hadoop and other typical applications from the Hadoop ecosystem. Apache Ambari is under a heavy development, and it will incorporate new features in a near future. For example Ambari is able to deploy a complete Hadoop system from scratch, however is not possible use this GUI in a Hadoop system that is already running. The ability to provisioning the operating system could be a good addition, however probably is not in the roadmap..

1. Apache Ambari
Apache Bigtop	
Bigtop was originally developed and released as an open source packaging infrastructure by Cloudera. BigTop is used for some vendors to build their own distributions based on Apache Hadoop (CDH, Pivotal HD, Intel’s distribution), however Apache Bigtop does many more tasks, like continuous integration testing (with Jenkins, maven, …) and is useful for packaging (RPM and DEB), deployment with Puppet, and so on. Apache Bigtop could be considered as a community effort with a main focus: put all bits of the Hadoop ecosystem as a whole, rather than individual projects.

1. Apache Bigtop.
Apache Helix	
Apache Helix is a generic cluster management framework used for the automatic management of partitioned, replicated and distributed resources hosted on a cluster of nodes. Originally developed by Linkedin, now is in an incubator project at Apache. Helix is developed on top of Zookeeper for coordination tasks. .

1. Apache Helix
Apache Mesos	
Mesos is a cluster manager that provides resource sharing and isolation across cluster applications. Like HTCondor, SGE or Troque can do it. However Mesos is hadoop centred design

1. Apache Mesos
Apache Slider	
Slider is a YARN application to deploy existing distributed applications on YARN, monitor them and make them larger or smaller as desired -even while the cluster is running.

1. Gihub page
Apache Whirr	
Apache Whirr is a set of libraries for running cloud services. It allows you to use simple commands to boot clusters of distributed systems for testing and experimentation. Apache Whirr makes booting clusters easy.

1. Apache Whirr
Apache YARN	
Apache Hadoop YARN is a sub-project of Hadoop at the Apache Software Foundation introduced in Hadoop 2.0 that separates the resource management and processing components. YARN was born of a need to enable a broader array of interaction patterns for data stored in HDFS beyond MapReduce. The YARN-based architecture of Hadoop 2.0 provides a more general processing platform that is not constrained to MapReduce.

1. Apache YARN
Brooklyn	
brooklyn is a library that simplifies application deployment and management. For deployment, it is designed to tie in with other tools, giving single-click deploy and adding the concepts of manageable clusters and fabrics: Many common software entities available out-of-the-box. Integrates with Apache Whirr – and thereby Chef and Puppet – to deploy well-known services such as Hadoop and elasticsearch (or use POBS, plain-old-bash-scripts) Use PaaS’s such as OpenShift, alongside self-built clusters, for maximum flexibility

Buildoop	
Buildoop is an open source project licensed under Apache License 2.0, based on Apache BigTop idea. Buildoop is a collaboration project that provides templates and tools to help you create custom Linux-based systems based on Hadoop ecosystem. The project is built from scrach using Groovy language, and is not based on a mixture of tools like BigTop does (Makefile, Gradle, Groovy, Maven), probably is easier to programming than BigTop, and the desing is focused in the basic ideas behind the buildroot Yocto Project. The project is in early stages of development right now.

1. Buildoop
Cloudera HUE	
Web application for interacting with Apache Hadoop.

Facebook Prism	
multi datacenters replication system

Google Borg	
job scheduling and monitoring system

1. Wired article
Google Omega	
job scheduling and monitoring system

1. Talk
Hortonworks HOYA	
HOYA is defined as “running HBase On YARN”. The Hoya tool is a Java tool, and is currently CLI driven. It takes in a cluster specification – in terms of the number of regionservers, the location of HBASE_HOME, the ZooKeeper quorum hosts, the configuration that the new HBase cluster instance should use and so on.

1. Hortonworks Blog
Marathon	
Marathon is a Mesos framework for long-running services. Given that you have Mesos running as the kernel for your datacenter, Marathon is the init or upstart daemon.

Applications
Apache Kiji	
Build Real-time Big Data Applications on Apache HBase.

Apache Nutch	
Highly extensible and scalable open source web crawler software project. A search engine based on Lucene: A Web crawler is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing. Web crawlers can copy all the pages they visit for later processing by a search engine that indexes the downloaded pages so that users can search them much more quickly.

Apache OODT	
OODT was originally developed at NASA Jet Propulsion Laboratory to support capturing, processing and sharing of data for NASA’s scientific archives

Apache Tika	
Toolkit detects and extracts metadata and structured text content from various documents using existing parser libraries.

1. Apache Tika
Eclipse BIRT	
BIRT is an open source Eclipse-based reporting system that integrates with your Java/Java EE application to produce compelling reports.

HIPI Library	
HIPI is a library for Hadoop’s MapReduce framework that provides an API for performing image processing tasks in a distributed computing environment.

Hunk	
Splunk analytics for Hadoop

1. Hunk
Jedox Palo	
Palo Suite combines all core applications — OLAP Server, Palo Web, Palo ETL Server and Palo for Excel — into one comprehensive and customisable Business Intelligence platform. The platform is completely based on Open Source products representing a high-end Business Intelligence solution which is available entirely free of any license fees.

MADlib	
The MADlib project leverages the data-processing capabilities of an RDBMS to analyze data. The aim of this project is the integration of statistical data analysis into databases. The MADlib project is self-described as the Big Data Machine Learning in SQL for Data Scientists. The MADlib software project began the following year as a collaboration between researchers at UC Berkeley and engineers and data scientists at EMC/Greenplum (now Pivotal)

1. MADlib Community
PivotalR	
PivotalR is a package that enables users of R, the most popular open source statistical programming language and environment to interact with the Pivotal (Greenplum) Database as well as Pivotal HD / HAWQ and the open-source database PostgreSQL for Big Data analytics. R is a programming language and data analysis software: you do data analysis in R by writing scripts and functions in the R programming language. R is a complete, interactive, object-oriented language: designed by statisticians, for statisticians. The language provides objects, operators and functions that make the process of exploring, modeling, and visualizing data a natural one.

1. 
Spango BI	
SpagoBI is an Open Source Business Intelligence suite, belonging to the free/open source SpagoWorld initiative, founded and supported by Engineering Group. It offers a large range of analytical functions, a highly functional semantic layer often absent in other open source platforms and projects, and a respectable set of advanced data visualization features including geospatial analytics

SparkR	
R frontend for Spark

1. AMPLab extras
Splunk	
analyzer for machine-generated date

1. Splunk
Talend	
Talend is an open source software vendor that provides data integration, data management, enterprise application integration and big data software and solutions.

Search engine and framework
Apache Lucene	
Search engine library

1. Apache Lucene
Apache Solr	
Search platform for Apache Lucene

1. Apache Solr
ElasticSearch	
Search and analytics engine based on Apache Lucene

1. ElasticSearch
Facebook Unicorn	
social graph search platform

Google Caffeine	
continuous indexing system

1. Google blog post
Google Percolator	
continuous indexing system

1. Paper
TeraGoogle	
large search index

1. 
HBase Comprocessor	
implementation of Percolator, part of HBase

1. HBase Comprocessor
LinkedIn Bobo	
is a Faceted Search implementation written purely in Java, an extension to Apache Lucene.

1. Github Page
LinkedIn Cleo	
Cleo is a flexible software library for enabling rapid development of partial, out-of-order and real-time typeahead search. It is suitable for data sets of varying sizes and types. Cleo has been used extensively to power LinkedIn typeahead search covering professional network connections, companies, groups, questions, skills and other site features.

1. Github
LinkedIn Galene	
search architecture at LinkedIn

1. Blog post on LinkedIn engineer
LinkedIn Zoie	
Zoie is a realtime search/indexing system written in Java.

1. Github
Sphnix Search Server	
Sphinx lets you either batch index and search data stored in an SQL database, NoSQL storage, or just files quickly and easily — or index and search data on the fly, working with Sphinx pretty much as with a database server.

1. Sphinx
MySQL forks and evolutions
Amazon RDS	
MySQL databases in Amazon’s cloud

1. Amazon RDS
Drizzle	
Drizzle is a re-designed version of the MySQL v6.0 codebase and is designed around a central concept of having a microkernel architecture. Features such as the query cache and authentication system are now plugins to the database, which follow the general theme of “pluggable storage engines” that were introduced in MySQL 5.1. It supports PAM, LDAP, and HTTP AUTH for authentication via plugins it ships. Via its plugin system it currently supports logging to files, syslog, and remote services such as RabbitMQ and Gearman. Drizzle is an ACID-compliant relational database that supports transactions via an MVCC design

Google Cloud SQL	
MySQL databases in Google’s cloud

1. Google Cloud SQL
MariaDB	
enhanced, drop-in replacement for MySQL

1. MariaDB
MySQL Cluster	
MySQL implementation using NDB Cluster storage engine

1. MySQL Cluster
Percona Server	
enhanced, drop-in replacement for MySQL

1. Percona Server
ProxySQL	
High Performance Proxy for MySQL

1. ProxySQL
TokuDB	
TokuDB is a storage engine for MySQL and MariaDB that is specifically designed for high performance on write-intensive workloads. It achieves this via Fractal Tree indexing. TokuDB is a scalable, ACID and MVCC compliant storage engine. TokuDB is one of the technologies that enable Big Data in MySQL.

WebScaleSQL	
is a collaboration among engineers from several companies that face similar challenges in running MySQL at scale, and seek greater performance from a database technology tailored for their needs.

1. Website
Memcached forks and evolutions
Facebook McDipper	
key/value cache for flash storage

1. Facebook McDipper
Facebook Memcached	
fork of Memcache

1. Facebook Memcached
Twemproxy	
A fast, light-weight proxy for memcached and redis

1. Github
Twitter Fatcache	
key/value cache for flash storage

1. Twitter Fatcache
Twitter Twemcache	
fork of Memcache

1. Twitter Twemcache
Embemmed Databases
BerkeleyDB	
a software library that provides a high-performance embedded database for key/value data

1. Oracle website
HanoiDB	
HanoiDB implements an indexed, key/value storage engine. The primary index is a log-structured merge tree (LSM-BTree) implemented using ‘doubling sizes’ persistent ordered sets of key/value pairs, similar is some regards to LevelDB. HanoiDB includes a visualizer which when used to watch a living database resembles the ‘Towers of Hanoi’ puzzle game, which inspired the name of this database.

1. Github
LevelDB	
a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values.

1. Google code website
LMDB	
ultra-fast, ultra-compact key-value embedded data store developed by Symas

1. Symas website
RocksDB	
RocksDB is an embeddable persistent key-value store for fast storage. RocksDB can also be the foundation for a client-server database but our current focus is on embedded workloads.

1. RocksDB site
Published with Amazon S3
