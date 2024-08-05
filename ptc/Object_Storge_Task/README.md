# object storage

## Object Storage and File Storage

![table][def4]

## S3

Amazon Simple Storage Service (S3) is a massively scalable storage service based on object storage technology. It provides a very high level of durability, with high availability and high performance. Data can be accessed from anywhere via the Internet, through the Amazon Console and the powerful S3 API.

**S3 storage provides the following key features:**

Buckets—data is stored in buckets. Each bucket can store an unlimited amount of unstructured data.
Elastic scalability—S3 has no storage limit. Individual objects can be up to 5TB in size.\
Flexible data structure—each object is identified using a unique key, and you can use metadata to flexibly organize data.\
Downloading data—easily share data with anyone inside or outside your organization and enable them to download data over the Internet.
Permissions—assign permissions at the bucket or object level to ensure only authorized users can access data.\
APIs – the S3 API, provided both as REST and SOAP interfaces, has become an industry standard and is integrated with a large number of existing tools.

### 5 Use Cases for S3 Storage

**1.Backup and Archival**\
One of the primary use cases for S3 storage is backup and archival. Organizations can leverage S3’s durability and availability to ensure the safety and longevity of their data. S3’s redundant architecture and distributed data storage make it possible to store critical data that needs to be accessed quickly and securely.

S3 also offers seamless integration with various backup and archival software. This allows businesses to automate the backup and archival processes, reducing the risk of human error and ensuring data is consistently protected. With S3’s versioning capabilities, organizations can also retain multiple versions of their files, enabling roll back to previous versions if needed.

**2.Content Distribution and Hosting**\
By leveraging S3’s global network of edge locations, content creators can distribute their files seamlessly to end-users, reducing latency and improving user experience. S3’s integration with content delivery networks (CDNs) further enhances its content distribution capabilities, ensuring that files are delivered quickly and efficiently.

Moreover, S3 storage is highly scalable, allowing businesses to handle high traffic spikes without performance degradation. This makes it an ideal choice for hosting static websites, where content is served directly from S3 buckets. With S3’s support for custom domain names and SSL certificates, businesses can create a reliable and secure web hosting environment.

**3.Disaster Recovery**\
With S3’s cross-region replication, businesses can automatically save their data in multiple Amazon regions, ensuring that it is protected against regional disasters. In the event of a disaster, organizations can quickly restore their data from the replicated copies stored in S3, minimizing downtime and data loss.

S3’s durability and availability also make it an excellent choice for storing backups of critical systems and databases. By regularly backing up data to S3, organizations can quickly recover their systems in the event of a failure, reducing the impact on business operations.

**4.Big Data and Analytics**\
S3’s low-cost storage object make it suitable for storing large volumes raw data. Organizations can ingest data from various sources into S3, including log files, sensor data, and social media feeds. S3’s integration with big data processing frameworks like Apache Hadoop and Apache Spark enables businesses to process and analyze this data at scale.

Additionally, S3 supports data lake architectures, allowing organizations to store structured and unstructured data in its native format. This reduces the need for data transformation, reducing complexity and enabling faster data processing. S3 tightly integrates with Amazon’s big data analytics services like Amazon Athena and Amazon Redshift.

**5.Software and Object Distribution**\
S3 is commonly used by organizations to distribute software packages, firmware updates, and other digital assets to users, customers, or employees. S3’s global network of edge locations ensures fast and efficient delivery of these files, regardless of the users’ location.

With S3’s support for access control policies and signed URLs, businesses can ensure that only authorized users can access their distributed files. This provides an additional layer of security and prevents unauthorized distribution or tampering of software packages.

### Buckets

Buckets are logical containers in which data is stored. S3 provides unlimited scalability, and there is no official limit on the amount of data and number of objects you can store in an S3 bucket. The size limit for objects stored in a bucket is 5 TB.

An S3 bucket name must be unique across all S3 users, because the bucket namespace is shared across all AWS accounts.

### Keys

When you upload an object to a bucket, the object gets a unique key. The key is a string that mimics a directory hierarchy. Once you know the key, you can access the object in the bucket.

The bucket name, key, and version ID uniquely identify every object in S3. S3 provides two URL structures you can use to directly access an object:

`{BUCKET-NAME}.s3.amazonaws.com/{OBJECT-KEY}`

`s3.amazon.aws.com/{BUCKET-NAME}/{OBJECT-KEY}`

## MinIO

Amazon S3 is a highly scalable and fully managed cloud storage solution provided by AWS, which offers extensive integrations, compliance, and a wide range of security features.\
 Minio, on the other hand, is a self-hosted open-source object storage server that provides cost-efficiency, flexibility, and control over data storage. The choice between the two depends on the specific requirements and priorities of the organization.

Deploy a working instance of MinIO using docker:

```bash
docker run -p 9000:9000 -p 9001:9001 --name minio1 -v D:\minio\data:/data -e "MINIO_ROOT_USER=ROOTUSER" -e "MINIO_ROOT_PASSWORD=CHANGEME123" quay.io/minio/minio server /data --console-address ":9001"
```

the result is:

![terminal][def3]

in docker desktop:

![docker-desktop][def2]

in chrome:

![in_chrome][def]

[def]: ./assets/9001.png
[def2]: ./assets/docker-minIO.png
[def3]: ./assets/docker-terminal.png
[def4]: ./assets/table_diff.png

We can upload objects from the visual Minio or from client.\
the code exit in client.js file.

for execute the code:

- run the command `docker run -it --rm --name server -p 8080:8080 -v ${pwd}:/app node`\
(with volume -v instead of WORKDIR)
- open terminal from Docker
- cd app directory
- run npm install.
- run the main file `node main.js`
