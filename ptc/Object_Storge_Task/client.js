import * as Minio from 'minio';
import dotenv from "dotenv";
import str from 'stream';

dotenv.config();

let connectToMinIO = (minioClient) => {
    try {
        minioClient = new Minio.Client({
            endPoint: process.env.HOST,
            port: parseInt(process.env.PORT),
            useSSL: false,
            accessKey: process.env.ACCESS_KEY,
            secretKey: process.env.SECRET_KEY
        })
    }
    catch (err) {
        throw err;
    }
}

let createBucket = async (minioClient, bucketName) => {
    try {
        await minioClient.makeBucket(bucketName, 'us-east-1', function (err) { });
    }
    catch (err) {
        throw err;
    }
}

let putObject = async (minioClient, bucketName, obj) => {
    try {
        let objStream = new str.Readable();
        objStream.push(JSON.stringify(obj));
        objStream.push(null);
        await minioClient.putObject(bucketName, obj.name, objStream, metaData = {}, function (err, objInfo) { return objInfo.versionId });
    }
    catch (err) {
        throw err;
    }
}

let listObjects = (minioClient, bucketName) => {
    try {
        const data = []
        const stream = minioClient.listObjects(bucketName, '', true)
        stream.on('data', function (obj) {
            data.push(obj)
        })
        stream.on('end', function (obj) {
            return data;
        })
    }
    catch (err) {
        throw err;
    }
}

let getObject = async (minioClient, bucketName, obj) => {
    try {
        let size = 0
        const dataStream = await minioClient.getObject(bucketName, obj.name)
        dataStream.on('data', function (chunk) {
            size += chunk.length
        })
        return dataStream;
    }
    catch (err) {
        throw err;
    }
}

let updateObjectTags = async (minioClient, bucketName, obj, tag) => {
    await minioClient.setObjectTagging(bucketName, obj.name, tag)
}

let removeObject = (minioClient, bucketName, obj) => {
    try {
        minioClient.removeObject(bucketName, obj.name)
    }
    catch (err) {
        throw err;
    }
}

module.exports = {
    connectToMinIO,
    createBucket,
    putObject,
    listObjects,
    getObject,
    updateObjectTags,
    removeObject
}
